# 16. HorizontalBarPlot.py
import matplotlib.pyplot as plt

categories = ['A', 'B', 'C', 'D']
values = [5, 7, 8, 6]

plt.barh(categories, values, color='purple')
plt.title('Horizontal Bar Plot')
plt.xlabel('Values')
plt.ylabel('Categories')
plt.show()
