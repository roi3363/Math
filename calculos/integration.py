import numpy as np
import matplotlib.pyplot as plt
from matplotlib import patches


def f(x):
    return x ** 2


n = 100
a, b = 0, 5
X = np.array([x for x in np.arange(a, b, (b - a) / n)])
Y = np.array([f(x) for x in np.arange(a, b, (b - a) / n)])
c = np.max(X)

intervals = np.array([(i, i + 1) for i in np.arange(a, b, (b - a) / n)])
sums = []
fig, ax = plt.subplots(1)
for i in intervals[:-1]:
    rect = patches.Rectangle((i[0], 0),  (b - a) / n, f(i[0]), linewidth=1, edgecolor='r', facecolor='none')
    ax.add_patch(rect)
    sums.append((b - a) / n * f(i[0]))
print(f'Area under the curve: {sum(sums)}')
plt.plot(X, Y)
plt.show()
