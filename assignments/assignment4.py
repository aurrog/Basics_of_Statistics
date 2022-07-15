import random

import matplotlib.pyplot as plt
import numpy as np


def mean(a):
    return sum(a) / len(a)


x = np.arange(0, 100)
y2 = [random.choices(x, k=10) for i in range(100)]
y = []
for i in y2:
    y.append(mean(i))

random.shuffle(y)
print(mean(x))
print(mean(y))

fig, ax = plt.subplots()

ax.bar(x, y)
plt.plot(x, y, c='red')
plt.plot(x, [i/2 for i in y], c='black')
plt.scatter(2, mean(x), c='green', s=150)

plt.show()
