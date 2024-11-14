# 33 AdvancedLinePlot.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, label='Sine', linestyle='--')
plt.plot(x, y2, label='Cosine', linestyle='-')
plt.title('Advanced Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
