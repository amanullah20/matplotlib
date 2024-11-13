# 22. PopulationPyramid.py
import matplotlib.pyplot as plt
import numpy as np

age_groups = ['0-10', '10-20', '20-30', '30-40', '40-50', '50-60']
male_population = np.array([100, 200, 300, 400, 300, 200])
female_population = np.array([150, 250, 350, 450, 350, 250])

plt.barh(age_groups, male_population, color='blue', label='Males')
plt.barh(age_groups, -female_population, color='pink', label='Females')

plt.xlabel('Population')
plt.title('Population Pyramid')
plt.legend()
plt.show()
