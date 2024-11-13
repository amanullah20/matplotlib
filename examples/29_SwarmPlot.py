# 29. SwarmPlot.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

data = sns.load_dataset('tips')
sns.swarmplot(x='day', y='total_bill', data=data, color='purple')
plt.title('Swarm Plot Example')
plt.show()
