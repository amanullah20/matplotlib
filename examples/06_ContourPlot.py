# 06. ContourPlot.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

plt.contour(X, Y, Z, levels=20, cmap='viridis')
plt.title('Contour Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
