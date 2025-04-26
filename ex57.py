# The ultimate tensile strength X of rope was studied (n = 16). (The rope is pulled until it breaks.) The mean was µ = 4482kg and the standard deviation σ = 115kg. Assume that X is normal distributed. Test the hypothesis µ0 = 4500kg compared to the hypothesis µ1 = 4400kg.
import math

# given values
n = 16
sample_mean = 4482
sigma = 115

# hypotheses
mu0 = 4500  # null hypothesis
mu1 = 4400  # alternative hypothesis

# standard error
se = sigma / math.sqrt(n)

# z statistics for both hypotheses
z_mu0 = (sample_mean - mu0) / se
z_mu1 = (sample_mean - mu1) / se

# critical values
z_5_percent = 1.96
z_1_percent = 2.58

print(f"standard error: {se:.2f}")
print(f"Z for mu0=4500: {z_mu0:.2f}")
print(f"Z for mu1=4400: {z_mu1:.2f}")

# check hypothesis for 5% significance level
print("\nchecking at 5% significance level:")
if abs(z_mu0) < z_5_percent:
    print("mu0 = 4500 accepted at 5% level.")
else:
    print("mu0 = 4500 rejected at 5% level.")

if abs(z_mu1) < z_5_percent:
    print("mu1 = 4400 accepted at 5% level.")
else:
    print("mu1 = 4400 rejected at 5% level.")

# check hypothesis for 1% significance level
print("\nchecking at 1% significance level:")
if abs(z_mu0) < z_1_percent:
    print("mu0 = 4500 accepted at 1% level.")
else:
    print("mu0 = 4500 rejected at 1% level.")

if abs(z_mu1) < z_1_percent:
    print("mu1 = 4400 accepted at 1% level.")
else:
    print("mu1 = 4400 rejected at 1% level.")
