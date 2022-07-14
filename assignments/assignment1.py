import math

x = 10
sd = 5
n = 100

se = sd / math.sqrt(n)

perc95 = 1.96
perc99 = 2.58

interval = [x - perc99 * se, x + perc99 * se]
print(interval)
