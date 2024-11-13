# 03. BoxenPlot.py
 import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = np.random.normal(size=1000)
sns.boxenplot(x=data)
plt.title('Boxen Plot Example')
plt.xlabel('Values')
plt.show()
