# 20. PieChartExploded.py
import matplotlib.pyplot as plt

sizes = [25, 35, 20, 20]
labels = ['A', 'B', 'C', 'D']
explode = (0.1, 0, 0, 0)

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, explode=explode)
plt.title('Exploded Pie Chart')
plt.show()
