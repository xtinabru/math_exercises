from scipy.stats import norm

mu = 5
sigma = 0.2

# (a) P(X <= k) = 0.95
k_a = norm.ppf(0.95, loc=mu, scale=sigma)

# (b) P(X > k) = 0.01 --> P(X <= k) = 0.99
k_b = norm.ppf(0.99, loc=mu, scale=sigma)

print(f"(a) k such that P(X <= k) = 95%: {k_a:.4f}")
print(f"(b) k such that P(X > k) = 1%: {k_b:.4f}")
