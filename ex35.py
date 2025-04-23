import math

products_checked = 2
accept_chance = 0.8

# mean and standard error (std deviation)
mean = products_checked * accept_chance
variance = products_checked * accept_chance * (1 - accept_chance)
std_dev = math.sqrt(variance)


# binomial distribution: P(0 accepted), P(1), P(2)
def accept_prob(k):
    return (
        math.comb(products_checked, k)
        * (accept_chance**k)
        * ((1 - accept_chance) ** (products_checked - k))
    )


# calculate and print results
distribution = {}
for accepted in range(products_checked + 1):
    distribution[accepted] = accept_prob(accepted)

print("Acceptance distribution for 2 products:\n")
for accepted, prob in distribution.items():
    print(f"{accepted} accepted: {prob:.5f}")

print(f"\nExpected accepted products (mean): {mean:.2f}")
print(f"Standard error (std deviation): {std_dev:.2f}")
