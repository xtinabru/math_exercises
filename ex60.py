# Two voltage meters differ by (in Volts): 0,4; -0,6; 0,2; 0,0; 1,0; 1,4; 0,4; 1,6. With significance level 5% can it be assumed that the calibration of the meters do not differ?

import math
import scipy.stats as st

# differences
differences = [0.4, -0.6, 0.2, 0.0, 1.0, 1.4, 0.4, 1.6]
# sample size
n = len(differences)

# sample mean
mean = sum(differences) / n

# sample standard deviation (unbiased)
std_dev = math.sqrt(sum((x - mean) ** 2 for x in differences) / (n - 1))

# Standard error
se = std_dev / math.sqrt(n)

# t-statistic
t_stat = (mean - 0) / se  # null hypothesis mean is 0

# critical t-value for two-tailed test
alpha = 0.05
t_critical = st.t.ppf(1 - alpha / 2, df=n - 1)

# results
print(f"Sample mean: {mean:.3f}")
print(f"Sample standard deviation: {std_dev:.3f}")
print(f"Standard error: {se:.3f}")
print(f"t statistic: {t_stat:.3f}")
print(f"Critical t value (5% level): {t_critical:.3f}")

# Decision
if abs(t_stat) < t_critical:
    print("Accepted. Calibration does not differ.")
else:
    print("Not accepted. Calibration differs.")
