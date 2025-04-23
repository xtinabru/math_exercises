# each outcome: (description, win in euros, probability)
outcomes = [("2 heads", 40, 1 / 4), ("1 head", 20, 2 / 4), ("2 tails", -100, 1 / 4)]

# expected value calculation
expected_value = sum(win * prob for _, win, prob in outcomes)

# output
print("Outcome probabilities and values:")
for desc, win, prob in outcomes:
    print(f"{desc}: {win} euros, probability = {prob:.2f}")

print(f"\nExpected value of the win: {expected_value:.2f} euros")
