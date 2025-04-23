# total
total_balls = 6
white_balls = 3
drawn_balls = 3

# expected value in hypergeometric distribution
expected_whites = drawn_balls * (white_balls / total_balls)

print(f"Expected number of white balls: {expected_whites:.2f}")
