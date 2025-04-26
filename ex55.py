# Average weight of a cell phone was announced to be 0.700kg. A sample of 10 phones was studied: 6 phones were 692g and 4 phones were 701g. Is the weight in the approved limits, if confidence of 99% is used?
import math

weights = [692, 701]  # weights in grams
counts = [6, 4]  # number of phones for each weight

# total number of phones
n = sum(counts)

# calculate the sample mean
mean = sum(w * c for w, c in zip(weights, counts)) / n

# calculate the sample variance
variance = sum(c * (w - mean) ** 2 for w, c in zip(weights, counts)) / (n - 1)

# standard deviation
std_dev = math.sqrt(variance)

# standard error of the mean
se = std_dev / math.sqrt(n)

# z-value for 99% confidence level
z = 2.58

# radius of the confidence interval
radius = z * se

# lower and upper bounds of the confidence interval
lower_bound = mean - radius
upper_bound = mean + radius

# results
print(f"sample mean: {mean:.1f} g")
print(f"confidence interval: {lower_bound:.1f} g to {upper_bound:.1f} g")

# check if the announced weight (700g) is within the confidence interval
if lower_bound <= 700 <= upper_bound:
    print("weight is within the approved limits.")
else:
    print("weight is NOT within the approved limits.")
