import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# === Load dataset ===
data_path = "data/leads.csv"

# Автоматическое создание CSV, если файла нет
if not os.path.exists(data_path):
    os.makedirs("data", exist_ok=True)
    with open(data_path, "w") as f:
        f.write("Lead,Stage,Value\nAcme Corp,Negotiation,25000\nNova AI,Discovery,15000\nGrowthLabs,Lost,8000\nHyperCRM,Closed Won,42000\n")

df = pd.read_csv(data_path)

# === Проверяем структуру данных ===
print("\n📊 Loaded dataset:\n", df.head())

# === Plot setup ===
plt.figure(figsize=(8, 5))
sns.set_theme(style="darkgrid")

# ВАЖНО: используем 'Value', а не 'DealValue'
sns.barplot(
    x="Stage",
    y="Value",
    hue="Lead",
    data=df,
    palette="coolwarm"
)

plt.title("CRM Deal Value by Stage", fontsize=14, fontweight="bold")
plt.xlabel("Stage", fontsize=12)
plt.ylabel("Deal Value ($)", fontsize=12)
plt.tight_layout()

# === Save chart ===
os.makedirs("outputs", exist_ok=True)
output_path = "outputs/visual_report.png"
plt.savefig(output_path, dpi=300)
plt.close()

print(f"\n✅ Visual report successfully created!\n📂 Saved to: {output_path}")
