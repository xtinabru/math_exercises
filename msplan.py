import matplotlib.pyplot as plt

# Суммарные значения на год по каждому каналу
channels = [
    "Social media advertisement",
    "Student influencers & collabs",
    "App store advertisement / Google UAC",
    "Content creation (visuals, blog)",
    "Email tools (Mailchimp)",
    "Other (analytics, landing, etc.)",
]

totals = [960, 600, 360, 240, 120, 120]

# Цвета (можно варьировать под настроение или важность)
colors = ["#66c2a5", "#fc8d62", "#8da0cb", "#e78ac3", "#a6d854", "#ffd92f"]

# Построение графика
plt.figure(figsize=(10, 6))
bars = plt.barh(channels, totals, color=colors)
plt.xlabel("Total Annual Budget (€)")
plt.title("TradeNova – Annual Marketing Budget by Channel")

# Добавим подписи к столбцам
for bar, value in zip(bars, totals):
    plt.text(
        value + 10,
        bar.get_y() + bar.get_height() / 2,
        f"{value} €",
        va="center",
        fontsize=9,
    )

plt.tight_layout()
plt.show()
