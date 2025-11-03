import json
from pathlib import Path
import pandas as pd

OUT_DIR = Path("outputs")
DATA_FILE = Path("data/leads.csv")
AI_FILE = OUT_DIR / "ai_insight.txt"
KPI_FILE = OUT_DIR / "kpi.json"
IMG_FILE = OUT_DIR / "visual_report.png"
MD_FILE  = OUT_DIR / "summary.md"

# Load
df = pd.read_csv(DATA_FILE)
with open(KPI_FILE, "r", encoding="utf-8") as f:
    kpis = json.load(f)
ai_text = AI_FILE.read_text(encoding="utf-8") if AI_FILE.exists() else "(no AI insight)"

# Nice tables
def df_to_md_table(frame: pd.DataFrame) -> str:
    return frame.to_markdown(index=False)

by_stage_items = [{"Stage": s, "Value": v} for s, v in kpis["by_stage"].items()]
by_stage_df = pd.DataFrame(by_stage_items)

top_deal = kpis["top_deal"]
top_df = pd.DataFrame([{"Lead": top_deal["Lead"], "Stage": top_deal["Stage"], "Value": top_deal["Value"]}])

# Compose markdown
md = []
md.append("# AI Decision Agent — Weekly Pipeline Report\n")
if IMG_FILE.exists():
    md.append(f"![Visual Report]({IMG_FILE.as_posix()})\n")

md.append("## Dataset Snapshot")
md.append(df.head(10).to_markdown(index=False))

md.append("\n## KPIs")
md.append(f"- Total pipeline: **${kpis['total_pipeline']:,.0f}**")
md.append(f"- Leads: **{kpis['n_leads']}**")

md.append("\n### Value by Stage")
md.append(df_to_md_table(by_stage_df))

md.append("\n### Top Deal")
md.append(df_to_md_table(top_df))

md.append("\n## AI Insights")
md.append(ai_text)

OUT_DIR.mkdir(parents=True, exist_ok=True)
MD_FILE.write_text("\n\n".join(md), encoding="utf-8")
print("✓ Summary generated:", MD_FILE)
