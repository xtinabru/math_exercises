import math

throws = 4
p = 1 / 6  # probability to get 6

# expected value and standard deviation
mean = throws * p
variance = throws * p * (1 - p)
std_dev = math.sqrt(variance)


# distr: probabilities for 0 to 4 sixes
def six_prob(k):
    return math.comb(throws, k) * (p**k) * ((1 - p) ** (throws - k))


distribution = {}
for k in range(throws + 1):
    distribution[k] = six_prob(k)

# output results
print("Distribution of number of sixes in 4 throws:\n")
for sixes, prob in distribution.items():
    print(f"{sixes} sixes: {prob:.5f}")

print(f"\nExpected value (mean): {mean:.2f}")
print(f"Standard deviation (std): {std_dev:.2f}")
