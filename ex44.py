# task44.py

import matplotlib.pyplot as plt
from scipy.stats import poisson
import numpy as np

# average number of computer breakdowns per month
lambda_ = 1  # Poisson parameter

# calculate P(X < 2) = P(X = 0) + P(X = 1)
prob_less_than_2 = poisson.cdf(1, lambda_)
print(f"P(X < 2) = {prob_less_than_2:.5f}")

# generate x values (possible number of breakdowns)
x = np.arange(0, 8)
pmf = poisson.pmf(x, lambda_)

# plot the Poisson distribution
plt.figure(figsize=(10, 6))
bars = plt.bar(x, pmf, alpha=0.7, label="Poisson PMF")

# highlight bars where X < 2
for i, bar in enumerate(bars):
    if x[i] < 2:
        bar.set_color("limegreen")
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
plt.title("Poisson Distribution (λ = 1): P(X < 2)")
plt.xlabel("Number of computer breakdowns in a month")
plt.ylabel("Probability")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
