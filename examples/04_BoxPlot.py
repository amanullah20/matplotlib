# 04. BoxPlot.py
import matplotlib.pyplot as plt
import numpy as np

data = [np.random.normal(0, std, 100) for std in range(1, 4)]

plt.boxplot(data, patch_artist=True)
plt.title('Box Plot Example')
plt.xlabel('Category')
plt.ylabel('Values')
plt.show()
