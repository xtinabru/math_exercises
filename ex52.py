# 52. Find the 99% confidence interval for the mean when the distribution is normal and σ = 2.5 with the sample: 30,8; 30,0; 29,9; 30,1; 31,7; 34,0.

import numpy as np
import scipy.stats as st

# numbers we have
data = [30.8, 30.0, 29.9, 30.1, 31.7, 34.0]
sigma = 2.5  # standard deviation
confidence = 0.99  # 99% confidence level

# find the average
average = np.mean(data)

# how many numbers
n = len(data)

# find the Z number for 99% confidence
z_value = st.norm.ppf(1 - (1 - confidence) / 2)

# find how much we add and subtract
step = z_value * sigma / np.sqrt(n)

# find the lower and upper numbers
low = average - step
high = average + step

# show the answer
print(f"Confidence interval: {low:.2f} <= mu <= {high:.2f}")
