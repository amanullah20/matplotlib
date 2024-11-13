# 17. LogarithmicPlot.py
import matplotlib.pyplot as plt
import numpy as np

x = np.logspace(0.1, 2, 100)
y = np.log(x)

plt.plot(x, y)
plt.xscale('log')
plt.title('Logarithmic Plot')
plt.xlabel('Log X-axis')
plt.ylabel('Log of X')
plt.show()
