# 12. FilledAreaPlot.py
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.fill_between(x, y, color='skyblue', alpha=0.4)
plt.plot(x, y, color='Slateblue')
plt.title('Filled Area Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
