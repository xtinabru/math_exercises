from scipy.stats import norm

# parameters
mu = 8
sigma = 1.7

# interval
x1 = 7
x2 = 12.2

# convert X to Z
z1 = (x1 - mu) / sigma
z2 = (x2 - mu) / sigma

# find the probability
prob = norm.cdf(z2) - norm.cdf(z1)
print(f"P(7 <= X <= 12.2) = {prob:.4f}")
