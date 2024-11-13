# 25. StackedBarPlot.py
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values1 = [5, 7, 8, 6]
values2 = [3, 6, 7, 4]

plt.bar(categories, values1, label='Category 1', color='lightblue')
plt.bar(categories, values2, bottom=values1, label='Category 2', color='orange')

plt.title('Stacked Bar Plot')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.legend()
plt.show()
