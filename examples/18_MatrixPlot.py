# 18. MatrixPlot.py
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = np.random.rand(10, 12)
sns.heatmap(data, annot=True, cmap='coolwarm')
plt.title('Matrix Plot Example')
plt.show()
