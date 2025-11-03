import os, json
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv

# ---------- Setup ----------
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OUT_DIR = Path("outputs"); OUT_DIR.mkdir(parents=True, exist_ok=True)
DATA_FILE = Path("data/leads.csv")
AI_FILE = OUT_DIR / "ai_insight.txt"
KPI_FILE = OUT_DIR / "kpi.json"

# ---------- Load data ----------
df = pd.read_csv(DATA_FILE)
# Expecting columns: Lead, Stage, Value
df["Value"] = pd.to_numeric(df["Value"], errors="coerce").fillna(0.0)

# ---------- KPIs ----------
total_pipeline = float(df["Value"].sum())
by_stage = (
    df.groupby("Stage")["Value"].sum().sort_values(ascending=False).to_dict()
)
top_deal = df.loc[df["Value"].idxmax()].to_dict()
kpis = {
    "total_pipeline": total_pipeline,
    "by_stage": by_stage,
    "top_deal": top_deal,
    "n_leads": int(len(df)),
}

# Save KPIs for reuse
with open(KPI_FILE, "w", encoding="utf-8") as f:
    json.dump(kpis, f, ensure_ascii=False, indent=2)

# ---------- AI insight ----------
def build_prompt(k):
    return f"""
You are a senior RevOps analyst. Given the pipeline KPIs (JSON below),
write 6–8 concise, actionable insights: where to focus, risks, quick wins,
and next best actions for the upcoming week. Be crisp and business-like.
Use bullets with short sentences. Prioritize $ value impact.
JSON:
{k}
"""

insight_text = (
    "OpenAI key not found. Skipping AI insight. "
    "Provide OPENAI_API_KEY in your env to enable this."
)

if OPENAI_API_KEY:
    try:
        # OpenAI Python SDK v1.x
        from openai import OpenAI
        client = OpenAI(api_key=OPENAI_API_KEY)

        prompt = build_prompt(json.dumps(kpis, ensure_ascii=False))
        resp = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role":"system","content":"You are a pragmatic, metric-driven RevOps consultant."},
                {"role":"user","content": prompt},
            ],
            max_tokens=450,
            temperature=0.2,
        )
        insight_text = resp.choices[0].message.content.strip()
    except Exception as e:
        insight_text = f"[AI error] {e}"

# ---------- Save ----------
with open(AI_FILE, "w", encoding="utf-8") as f:
    f.write(insight_text)

print("✓ AI insight saved to:", AI_FILE)
print("✓ KPIs saved to:", KPI_FILE)
