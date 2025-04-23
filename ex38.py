total_tickets = 1000

# list of (net win, how many tickets have this win)
prizes = [
    (99, 1),  # 100e win → net win = 99
    (49, 10),  # 50e win → net win = 49
    (19, 15),  # 20e win → net win = 19
    (-1, 974),  # no win → net loss = -1 (cost of ticket)
]

# calculate expected value
expected_value = sum(net_win * count for net_win, count in prizes) / total_tickets

print(f"Expected net win per ticket: {expected_value:.2f} euros")
