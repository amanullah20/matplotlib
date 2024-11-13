# 26. StemPlot.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 20)
y = np.cos(x)

plt.stem(x, y, linefmt='g-', markerfmt='go', basefmt='r-')
plt.title('Stem Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
