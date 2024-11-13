# 09. DonutChart.py
import matplotlib.pyplot as plt

sizes = [25, 35, 20, 20]
labels = ['A', 'B', 'C', 'D']

plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.4))
plt.title('Donut Chart')
plt.show()
