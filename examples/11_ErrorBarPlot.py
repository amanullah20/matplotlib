# 11. ErrorBarPlot.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 10)
y = np.sin(x)
yerr = 0.1 + 0.1 * np.sqrt(x)

plt.errorbar(x, y, yerr=yerr, fmt='o', color='black', ecolor='red', elinewidth=1, capsize=2)
plt.title('Error Bar Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
