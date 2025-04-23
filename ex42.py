import matplotlib.pyplot as plt
from scipy.stats import poisson
import numpy as np

# Poisson parameter (λ = n * p)
lambda_ = 900 * 0.007

# (a) probability that exactly 7 controllers fail
prob_7 = poisson.pmf(7, lambda_)
print(f"(a) P(X = 7) = {prob_7:.5f}")

# (b) probability that more than 3 controllers fail
prob_more_than_3 = 1 - poisson.cdf(3, lambda_)
print(f"(b) P(X > 3) = {prob_more_than_3:.5f}")

# GRAPHING
# generate values for the x-axis (number of failures)
x = np.arange(0, 20)
pmf_values = poisson.pmf(x, lambda_)

# plot the Poisson distribution with annotations
plt.figure(figsize=(10, 6))
bars = plt.bar(x, pmf_values, alpha=0.7, label="Poisson PMF")

# annotate each bar with its probability value
for i, bar in enumerate(bars):
    height = bar.get_height()
    if height > 0.01:  # show only meaningful values
        plt.text(
            bar.get_x() + bar.get_width() / 2.0,
            height,
            f"{height:.2f}",
            ha="center",
            va="bottom",
        )

# add vertical lines for reference
plt.axvline(7, color="red", linestyle="--", label="X = 7")
plt.axvline(3, color="green", linestyle="--", label="X = 3")

# plot formatting
plt.title("Poisson Distribution (λ = 6.3) with Annotated Probabilities")
plt.xlabel("Number of controller failures")
plt.ylabel("Probability")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
