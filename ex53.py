# Find the 95% confidence interval for the mean when the distribution is normal. It is known that µ = 74.81 and σ = 4 when n = 200.

import math

mean = 74.81  # the average
sigma = 4  # standard deviation
n = 200  # number of samples
confidence = 0.95  # 95% confidence level

# z-value for 95% confidence
z = 1.96

# find standard error
se = sigma / math.sqrt(n)

# find how much to add and subtract
step = z * se

# find the lower and upper bounds
lower = mean - step
upper = mean + step

# result
print(f"Confidence interval: {lower:.2f} <= mean <= {upper:.2f}")
