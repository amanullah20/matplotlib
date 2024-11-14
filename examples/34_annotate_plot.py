# 34 AnnotatedPlot.py
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [3, 7, 2, 5, 8]

plt.plot(x, y, marker='o')
plt.annotate('Highest Point', xy=(5, 8), xytext=(3, 9),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.title('Annotated Plot Example')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid(True)
plt.show()
