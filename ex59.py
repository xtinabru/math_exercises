# Let X ∼ N(µ, σ2). Test the hypothesis µ0 = 55 with the significance level 5% for the sample

import math
import scipy.stats as st

sample = [
    53.08,
    56.02,
    57.32,
    51.76,
    57.07,
    59.08,
    59.00,
    52.31,
    54.10,
    55.78,
    54.91,
    60.50,
    56.81,
    56.72,
    58.13,
    58.31,
    58.85,
    54.92,
    60.69,
    58.70,
]

mu0 = 55
alpha = 0.05

# sample size
n = len(sample)

# sample mean
mean = sum(sample) / n

# sample standard deviation (unbiased, so ddof=1)
std_dev = math.sqrt(sum((x - mean) ** 2 for x in sample) / (n - 1))

# standard error
se = std_dev / math.sqrt(n)

# t-statistic
t_stat = (mean - mu0) / se

# critical t-value for two-tailed test
t_critical = st.t.ppf(1 - alpha / 2, df=n - 1)

# results
print(f"Sample mean: {mean:.2f}")
print(f"Sample standard deviation: {std_dev:.2f}")
print(f"Standard error: {se:.2f}")
print(f"t statistic: {t_stat:.2f}")
print(f"Critical t value (5% level): {t_critical:.2f}")

# decision
if abs(t_stat) < t_critical:
    print("Accepted.")
else:
    print("Not accepted.")
