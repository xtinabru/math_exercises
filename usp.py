import pandas as pd
import matplotlib.pyplot as plt

# Define the comparison criteria
criteria = [
    "Beginner-friendly experience",
    "Realistic trading environment",
    "Risk-free learning",
    "Hands-on learning design",
    "Real learning from real market data",
]

# Ratings on a scale from 1 to 10 for each product
data = {
    "Criterion": criteria,
    "TradeNova (You)": [9, 8, 10, 9, 9],
    "Investopedia Simulator": [6, 7, 9, 5, 7],
    "Trading 212": [7, 8, 8, 6, 7],
    "eToro": [5, 7, 6, 5, 6],
}

# Create a DataFrame for plotting
df = pd.DataFrame(data)

# Create the line plot
plt.figure(figsize=(12, 6))
for column in df.columns[1:]:
    plt.plot(df["Criterion"], df[column], marker="o", label=column)

# Customize the plot
plt.title("USP Analysis: TradeNova vs Competitors")
plt.xlabel("Criteria")
plt.ylabel("Score (1–10)")
plt.ylim(0, 10)
plt.grid(True)
plt.xticks(rotation=30)
plt.legend()
plt.tight_layout()

# Display the plot
plt.show()
