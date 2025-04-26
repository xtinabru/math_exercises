# Find the confidence intervals for X with confidences 95%, 99% and 99.9%.
import math

# given data (waiting times in minutes)
data = [
    97.0,
    101.5,
    102.1,
    103.9,
    93.4,
    103.3,
    104.1,
    98.6,
    97.3,
    96.2,
    107.7,
    104.8,
    98.5,
    99.2,
    93.8,
    100.3,
    103.7,
    96.4,
]

# given standard deviation
sigma = 25

# sample size
n = len(data)

# sample mean
mean = sum(data) / n

# standard error of the mean
se = sigma / math.sqrt(n)

# z-values for different confidence levels
z_values = {"95%": 1.96, "99%": 2.58, "99.9%": 3.29}

# calculate and print confidence intervals
for confidence, z in z_values.items():
    radius = z * se
    lower_bound = mean - radius
    upper_bound = mean + radius
    print(
        f"{confidence} confidence interval: {lower_bound:.2f} min to {upper_bound:.2f} min"
    )
