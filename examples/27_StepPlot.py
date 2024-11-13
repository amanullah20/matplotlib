# 27. StepPlot.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 10)
y = np.exp(x)

plt.step(x, y, where='mid', label='Exponential Growth')
plt.title('Step Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.show()
