from scipy.stats import norm

mu = 175
sigma = 8
x = 200

z = (x - mu) / sigma

# calculate the probability
prob = 1 - norm.cdf(z)

print(f"P(X > 200) = {prob:.6f}")
