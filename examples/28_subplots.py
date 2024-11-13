# 28. Subplots.py
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [2, 4, 6, 8, 10]
y2 = [1, 3, 5, 7, 9]

fig, ax = plt.subplots(2, 1)  # 2 rows, 1 column
ax[0].plot(x, y1, 'r-')
ax[0].set_title('First Plot')

ax[1].bar(x, y2, color='blue')
ax[1].set_title('Second Plot')

plt.tight_layout()
plt.show()
