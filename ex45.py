from scipy.stats import norm

# (a) P(z <= 0.25)
prob_a = norm.cdf(0.25)
print(f"(a) P(z <= 0.25) = {prob_a:.4f}")

# (b) P(1.2 <= z <= 2.1)
prob_b = norm.cdf(2.1) - norm.cdf(1.2)
print(f"(b) P(1.2 <= z <= 2.1) = {prob_b:.4f}")

# (c) P(-1 <= z <= 1.5)
prob_c = norm.cdf(1.5) - norm.cdf(-1)
print(f"(c) P(-1 <= z <= 1.5) = {prob_c:.4f}")
