# 24. ScatterPlot.py
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 14, 18, 22, 26]

plt.scatter(x, y, color='red', marker='o')
plt.title('Scatter Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
