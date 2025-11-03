![AI Decision Agent](https://github.com/daria-lebed/ai-decision-agent/blob/main/docs/banner.png)

# 🧠 AI Decision Agent — CRM Analytics & Smart RevOps Dashboard

AI-powered RevOps assistant that analyzes CRM data, extracts insights, and builds automated reports — combining metrics, visuals, and GPT recommendations for fast data-driven decisions.

---
## ⚙️ Features

- 📊 Auto-generated pipeline visuals (`visual_report.png`)
- 🧩 AI-powered insight generation via GPT-4o-mini
- 💼 KPI & Stage-based performance breakdown
- 🪄 Exports full Markdown summary (`summary.md`) with insights and recommendations
- 🔁 Modular pipeline for automation & integration with HubSpot or Google Sheets

---

## 💻 Tech Stack

## 🧠 Tech Stack

<p align="left">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-original.svg" width="48" height="48" alt="Python"/>
  <img src="https://upload.wikimedia.org/wikipedia/commons/4/4d/OpenAI_Logo.svg" width="48" height="48" alt="OpenAI"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/pandas/pandas-original.svg" width="48" height="48" alt="Pandas"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/matplotlib/matplotlib-original.svg" width="48" height="48" alt="Matplotlib"/>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original.svg" width="48" height="48" alt="GitHub"/>
</p>

| Layer | Tools |
|-------|--------|
| Language | Python |
| AI | OpenAI GPT-4o-mini |
| Data | Pandas |
| Workflow | Modular pipelines |
| Output | CSV + AI summaries |
---
## 🧱 Project Structure

ai-decision-agent/
├── data/
│   └── leads.csv
├── src/
│   ├── visual_report.py
│   ├── ai_insight.py
│   └── generate_summary.py
├── outputs/
│   ├── visual_report.png
│   ├── ai_insight.txt
│   ├── kpi.json
│   └── summary.md
└── README.md

---
## 🧩 Installation

```bash
# Clone the repository
git clone https://github.com/daria-lebed/ai-decision-agent.git
cd ai-decision-agent

# Create virtual environment & install dependencies
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Run AI agent
python src/ai_insight.py
```
---

🧾 License

Distributed under the MIT License.
See LICENSE for more information.

⸻

Built by Daria Lebed￼https://www.linkedin.com/in/dioraswan/
AI-powered RevOps Automation • November 2025

