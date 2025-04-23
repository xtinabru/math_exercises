from scipy.stats import norm

mu = 80
sigma = 4

# (a) P(77 <= X <= 80)
z1 = (77 - mu) / sigma  # -0.75
z2 = (80 - mu) / sigma  # 0
prob_a = norm.cdf(z2) - norm.cdf(z1)
print(f"(a) P(77 <= X <= 80) = {prob_a:.4f}")

# (b) P(X > 80)
prob_b = 1 - norm.cdf((80 - mu) / sigma)  # Z = 0
print(f"(b) P(X > 80) = {prob_b:.4f}")
