# Let X ∼ N(µ, σ = 60). Test the hypothesis µ0 = 120 with the sample

import math

sample = [
    115,
    125,
    102,
    129,
    121,
    119,
    120,
    120,
    126,
    120,
    124,
    118,
    116,
    132,
    114,
    108,
    127,
    131,
    130,
    181,
]

sigma = 60
mu0 = 120

# sample size
n = len(sample)

# sample mean
mean = sum(sample) / n

# standard error
se = sigma / math.sqrt(n)

# Z-statistic
z = (mean - mu0) / se

# critical Z values
z_5_percent = 1.96
z_1_percent = 2.58
z_0_1_percent = 3.29

# results
print(f"sample mean: {mean:.2f}")
print(f"standard error: {se:.2f}")
print(f"Z statistic: {z:.2f}")

# Check acceptance
print("\nDecision:")
if abs(z) < z_5_percent and abs(z) < z_1_percent and abs(z) < z_0_1_percent:
    print("Accepted with all significance levels.")
else:
    print("Rejected at some significance level.")
