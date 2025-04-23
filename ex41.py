from collections import Counter
import matplotlib.pyplot as plt

# number of heads in 90 experiments
heads_counts = [
    0,
    2,
    3,
    2,
    4,
    3,
    4,
    3,
    3,
    4,
    1,
    4,
    3,
    4,
    5,
    3,
    4,
    4,
    4,
    3,
    2,
    1,
    4,
    2,
    3,
    4,
    2,
    5,
    3,
    4,
    4,
    2,
    4,
    2,
    1,
    2,
    4,
    2,
    1,
    2,
    4,
    1,
    4,
    3,
    2,
    1,
    4,
    3,
    2,
    2,
    1,
    5,
    2,
    3,
    1,
    5,
    3,
    3,
    1,
    3,
    4,
    2,
    3,
    4,
    2,
    3,
    4,
    1,
    3,
    5,
    5,
    3,
    2,
    5,
    2,
    3,
    2,
    3,
    4,
    4,
    2,
    3,
    3,
    2,
    3,
    4,
    5,
    0,
    5,
    2,
    3,
    3,
    4,
    3,
    0,
    4,
    1,
    2,
    4,
]

# count frequencies
distribution = Counter(heads_counts)
sorted_distribution = dict(sorted(distribution.items()))

# print distribution
print("Distribution of number of heads (out of 6 coins):\n")
for heads, count in sorted_distribution.items():
    print(f"{heads} heads: {count} times")

# graph the distribution
x = list(sorted_distribution.keys())
y = list(sorted_distribution.values())

plt.bar(x, y, color="skyblue", edgecolor="black")
plt.title("Distribution of Number of Heads (90 trials, 6 coins)")
plt.xlabel("Number of Heads")
plt.ylabel("Frequency")
plt.xticks(range(0, 7))
plt.grid(axis="y", linestyle="--", alpha=0.5)
plt.tight_layout()
plt.show()
