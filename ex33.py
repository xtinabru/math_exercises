# given expected value and variance
mean = 2
target_variance = 4 / 3

# brute-force: try values of n from 1 to 20
for n in range(1, 21):
    p = mean / n
    if p > 1:
        continue
    # skip invalid probabilities

    variance = n * p * (1 - p)

    # сheck if variance matches the target (allowing small error)
    if abs(variance - target_variance) < 1e-6:
        print(" The matching values:")
        print(f"   n = {n}")
        print(f"   p = {p:.5f}")
        print(f"   variance = {variance:.5f}")
        print(f"   (matches target variance = {target_variance})")
        break
