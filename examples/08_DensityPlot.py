# 08. DensityPlot.py
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = np.random.normal(0, 1, 1000)
sns.kdeplot(data, shade=True, color='green')
plt.title('Density Plot')
plt.xlabel('Value')
plt.ylabel('Density')
plt.show()
