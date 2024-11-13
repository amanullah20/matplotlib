# 05. ConnectedScatterPlot.py
import matplotlib.pyplot as plt
import numpy as np

x = np.random.rand(10)
y = np.random.rand(10)

plt.plot(x, y, marker='o')
for i in range(len(x)-1):
    plt.annotate('', xy=(x[i+1], y[i+1]), xytext=(x[i], y[i]), arrowprops=dict(arrowstyle='->', lw=1))

plt.title('Connected Scatter Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
