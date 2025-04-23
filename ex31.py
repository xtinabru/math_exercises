import math
import matplotlib.pyplot as plt

spins = 3  # number of times the wheel is spun
p = 1 / 8  # probability of landing on the joker in one spin


# calculate the probability of getting exactly j jokers
def prob(j):
    return math.comb(spins, j) * (p**j) * ((1 - p) ** (spins - j))


# dictionary to store the probabilities for 0, 1, 2, 3 jokers
chances = {}
for j in range(spins + 1):
    chances[j] = prob(j)

# calculate the expected number of jokers
expected = sum(j * chances[j] for j in chances)

print("Chances per number of jokers:\n")
for j in chances:
    print(f"{j} jokers: {chances[j]:.5f}")

# Print the expected value
print(f"\nExpected jokers: {expected:.3f}")

# Plotting the results
plt.bar(chances.keys(), chances.values())
plt.title("Jokers in 3 Spins")
plt.xlabel("Number of Jokers")
plt.ylabel("Probability")
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.show()
