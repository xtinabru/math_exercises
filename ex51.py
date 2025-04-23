from scipy.stats import norm

mu = 3
sigma = 0.1

# (a) P(2.9 <= X <= 3.05)
z1_a = (2.9 - mu) / sigma
z2_a = (3.05 - mu) / sigma
prob_a = norm.cdf(z2_a) - norm.cdf(z1_a)

# (b) P(X > 2.95)
z_b = (2.95 - mu) / sigma
prob_b = 1 - norm.cdf(z_b)

# (c) P(X < 2.83)
z_c = (2.83 - mu) / sigma
prob_c = norm.cdf(z_c)

print(f"(a) P(2.9 <= X <= 3.05) = {prob_a:.4f}")
print(f"(b) P(X > 2.95) = {prob_b:.4f}")
print(f"(c) P(X < 2.83) = {prob_c:.4f}")
