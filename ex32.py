import math

shots = 2
score_chance = 0.7


# function to calculate the chance of getting exactly successful throws
def score_probability(scored):
    return (
        math.comb(shots, scored)
        * (score_chance**scored)
        * ((1 - score_chance) ** (shots - scored))
    )


# store chances for 0, 1, or 2 scores
score_chances = {}
for scored in range(shots + 1):
    score_chances[scored] = score_probability(scored)

# calculate the average number of scores
expected_score = sum(scored * chance for scored, chance in score_chances.items())

print("Chances for each number of successful throws:\n")
for scored, chance in score_chances.items():
    print(f"{scored} scores: {chance:.4f}")

print(f"\nExpected number of scores: {expected_score:.2f}")
