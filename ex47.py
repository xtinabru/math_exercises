from scipy.stats import norm

print("Debug: script started")

mu = 3
sigma = 1.2
x = 5
n = 7000

z = (x - mu) / sigma
print(f"Debug: z = {z}")

prob = 1 - norm.cdf(z)
print(f"Debug: prob = {prob}")

expected_batteries = n * prob
print(f"P(X > 5) = {prob:.4f}")
print(
    f"Expected number of batteries that last more than 5 years: {expected_batteries:.0f}"
)
