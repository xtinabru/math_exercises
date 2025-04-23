import itertools

# list of envelope values
envelopes = [10, 20, 30, 40, 50]

# all combinations of 2 envelopes
pairs = list(itertools.combinations(envelopes, 2))

# calculate the sum for each pair
pair_sums = [sum(pair) for pair in pairs]

# calculate expected value (average of all possible totals)
expected_value = sum(pair_sums) / len(pair_sums)

# output
print("All possible sums from picking 2 envelopes:")
for pair, total in zip(pairs, pair_sums):
    print(f"{pair} -> {total} euros")


print(f"\nExpected value (average total): {expected_value:.2f} euros")
