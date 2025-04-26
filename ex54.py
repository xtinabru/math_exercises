# Laptop should have average weight of at least 2,0kg. Sample contains the weights: 8 laptops 1,90kg, 10 laptops 1,95kg, 12 laptops 1,98kg and 4 laptops 2,05kg. How much underweight the products are if confidence of 95% is used?

import math

weights = [1.90, 1.95, 1.98, 2.05]
counts = [8, 10, 12, 4]

n = sum(counts)
mean = sum(w * c for w, c in zip(weights, counts)) / n
variance = sum(c * (w - mean) ** 2 for w, c in zip(weights, counts)) / n
std_dev = math.sqrt(variance)
se = std_dev / math.sqrt(n)
z = 1.96
lower = mean - z * se

# Find underweight in grams
underweight_grams = max(0, (2.0 - lower)) * 1000

print(f"Underweight: {underweight_grams:.0f} g")
