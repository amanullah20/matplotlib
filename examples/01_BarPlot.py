# 01. BarPlot.py
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [5, 7, 8, 6]

plt.bar(categories, values, color='green')
plt.title('Bar Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
