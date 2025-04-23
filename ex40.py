# each coin type
coins = {0.5: 2, 1.0: 6, 2.0: 4}

total = sum(coins.values())

# calculate probabilities
distribution = {value: count / total for value, count in coins.items()}

# output the distribution
print("Probability distribution of randomly picked coin:\n")
for value, prob in sorted(distribution.items()):
    print(f"€{value:.2f} coin: {prob:.4f}")
