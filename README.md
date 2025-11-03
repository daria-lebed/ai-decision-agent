# 🤖 AI Decision Agent

AI-powered RevOps assistant that analyzes CRM data, extracts insights, and builds automated reports — combining analytics and GPT intelligence for fast, data-driven decisions.

---

## ✨ Features
- 📊 Auto-generated pipeline visuals (`visual_report.png`)
- 🧠 AI-powered insight generation via GPT-4o-mini
- 📈 KPI & Stage-based performance breakdown
- 📝 Exports Markdown summaries (`summary.md`) with insights and recommendations
- 🔁 Modular pipeline for automation & HubSpot/Google Sheets integration
  
---

## 💻 Tech Stack

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="42" height="42" alt="Python"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="42" height="42" alt="Pandas"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matplotlib/matplotlib-original.svg" width="42" height="42" alt="Matplotlib"/>
</p>

| Layer | Tools |
|-------|--------|
| **Language** | Python |
| **AI** | OpenAI GPT-4o-mini |
| **Data** | Pandas |
| **Visualization** | Matplotlib, Seaborn |
| **Workflow** | Modular Pipelines |
| **Output** | CSV + AI summaries |

---

## 📁 Project Structure

```bash
ai-decision-agent/
├── data/                     # Input data folder
│   └── leads.csv             # Sample CRM leads (Name, Stage, Value)
│
├── src/                      # Core logic and analytics scripts
│   ├── ai_insight.py         # Generates AI-powered insights using GPT-4o-mini
│   ├── visual_report.py      # Builds visual sales reports and charts
│   └── generate_summary.py   # Exports summaries and KPI breakdowns
│
├── outputs/                  # Auto-generated analysis results
│   ├── visual_report.png     # Pipeline visualization
│   ├── ai_insight.txt        # Plain-text insight summary
│   ├── kpi.json              # Structured metrics for automation
│   └── summary.md            # Markdown report for sharing
│
└── README.md
```
---
## ⚙️ Installation

To set up and run the **AI Decision Agent** locally:

```bash
# 1️⃣ Clone the repository
git clone https://github.com/daria-lebed/ai-decision-agent.git
cd ai-decision-agent

# 2️⃣ Create a virtual environment
python3 -m venv venv
source venv/bin/activate    # On macOS / Linux
# .\venv\Scripts\activate   # On Windows

# 3️⃣ Install dependencies
pip install -r requirements.txt
```
---
💡 Usage Example

Once the environment is ready, you can generate insights or reports automatically.
```bash
# Run AI-powered insight generation
python src/ai_insight.py

# Generate visual pipeline report
python src/visual_report.py

# Create summarized KPI and Markdown report
python src/generate_summary.py
```

✅ Outputs are stored in the /outputs/ folder:

	•	visual_report.png — visualized pipeline chart
	•	ai_insight.txt — text-based GPT analysis
	•	kpi.json — performance metrics
	•	summary.md — executive-style report

⸻

## ✨ Project Highlights

- 🚀 **AI-powered RevOps automation** — transforms CRM data into real-time insights and visual analytics.  
- 🧠 **GPT-4o-mini decision engine** — interprets leads, stages, and values to recommend next actions.  
- 📊 **Instant visualization** — automatically creates pipeline charts and KPI summaries for team reports.  
- ⚡ **No-code ready integration** — works seamlessly with HubSpot, Google Sheets, or internal dashboards.  
- 🧩 **Modular architecture** — easy to extend with additional AI models, APIs, or automation scripts.

⸻

Built by Daria Lebed￼https://www.linkedin.com/in/dioraswan/
AI-powered RevOps Automation • November 2025

⸻
