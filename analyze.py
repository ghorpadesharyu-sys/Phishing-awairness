import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
df = pd.read_csv(BASE / "data" / "demo_results.csv")
n = len(df)

metrics = {
    "Participants": n,
    "Link click rate (%)": round(df["clicked_link"].mean()*100, 1),
    "Data-entry attempt rate (%)": round(df["attempted_demo_data"].mean()*100, 1),
    "Report rate (%)": round(df["reported_simulation"].mean()*100, 1),
}
print(metrics)

labels = ["Clicked link", "Demo data-entry", "Reported"]
values = [
    df["clicked_link"].sum(),
    df["attempted_demo_data"].sum(),
    df["reported_simulation"].sum()
]
plt.figure(figsize=(7,4.5))
plt.bar(labels, values)
plt.ylabel("Participants")
plt.title("Phishing Awareness Simulation – Demonstration Results")
plt.tight_layout()
plt.savefig(BASE / "docs" / "demonstration_results_chart.png", dpi=180)
plt.show()
