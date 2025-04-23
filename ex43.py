# task43.py
import matplotlib.pyplot as plt
from scipy.stats import poisson
import numpy as np

# what we have:  on average 2 cars arrive per minute
lambda_ = 2  # Poisson parameter

# calculate P(X >= 4)
# this is equal to 1 - P(X <= 3)
prob_4_or_more = 1 - poisson.cdf(3, lambda_)
print(f"P(X >= 4) = {prob_4_or_more:.5f}")


# prepare x values (number of cars)
x = np.arange(0, 11)
pmf = poisson.pmf(x, lambda_)

# plot the Poisson distribution
plt.figure(figsize=(10, 6))
bars = plt.bar(x, pmf, alpha=0.7, label="Poisson PMF")

# highlight bars for X >= 4 in orange
for i, bar in enumerate(bars):
    if x[i] >= 4:
        bar.set_color("orange")
    height = bar.get_height()
    if height > 0.01:
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height,
            f"{height:.2f}",
            ha="center",
            va="bottom",
        )

# add labels and formatting
plt.title("Poisson Distribution (λ = 2): P(X ≥ 4)")
plt.xlabel("Number of cars arriving in a minute")
plt.ylabel("Probability")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
