# . Assume X ∼ N(µ, σ = 3). Compare the hypothesis µ0 = 60.0 and µ1 = 57.0 with sample size n = 20, mean µ = 58.05 and by choosing significance level α = 5%.

import math

# values
sigma = 3  # standard deviation
n = 20  # sample size
sample_mean = 58.05  # sample mean
mu0 = 60.0  # nll hypothesis mean
mu1 = 57.0  # aternative hypothesis mean
alpha = 0.05  # significance level

# calculate standard error
se = sigma / math.sqrt(n)

# calculate Z statistic for mu0
z_mu0 = (sample_mean - mu0) / se

# critical Z value for two-tailed test
z_critical = 1.96

#  results
print(f"Standard error: {se:.2f}")
print(f"Z statistic for mu0: {z_mu0:.2f}")
print(f"Critical Z value: {z_critical}")

# decision
if abs(z_mu0) > z_critical:
    print("mu0 = 60.0 rejected, mu1 = 57.0 accepted")
else:
    print("mu0 = 60.0 accepted, mu1 = 57.0 rejected")
