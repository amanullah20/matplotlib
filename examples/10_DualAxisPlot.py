# 10. DualAxisPlot.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.exp(x)
y2 = np.log(x + 1)

fig, ax1 = plt.subplots()
ax2 = ax1.twinx()

ax1.plot(x, y1, 'g-')
ax2.plot(x, y2, 'b-')

ax1.set_xlabel('X-axis')
ax1.set_ylabel('Exponential', color='g')
ax2.set_ylabel('Logarithm', color='b')

plt.title('Dual Axis Plot')
plt.show()
