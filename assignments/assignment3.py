import math

x = 18.5
sd = 4
n = 64

se = sd / math.sqrt(n)

perc95 = 1.96
perc99 = 2.58

interval = [x - perc95 * se, x + perc95 * se]
print(interval)

interval = [x - perc99 * se, x + perc99 * se]
print(interval)
