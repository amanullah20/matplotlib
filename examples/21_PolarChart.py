# 21. PolarChart.py
import matplotlib.pyplot as plt
import numpy as np

theta = np.linspace(0, 2*np.pi, 100)
r = np.abs(np.sin(3 * theta))

plt.polar(theta, r)
plt.title('Polar Chart')
plt.show()
