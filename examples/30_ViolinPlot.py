# 30. ViolinPlot.py
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = np.random.normal(size=(20, 4)) + np.arange(4) * 2
sns.violinplot(data=data)
plt.title('Violin Plot Example')
plt.xlabel('Categories')
plt.ylabel('Values')
plt.show()
