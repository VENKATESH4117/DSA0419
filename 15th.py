import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

import scipy.stats as stats

age = [23, 23, 27, 27, 39, 41, 47, 49, 50, 52, 54, 54, 56, 57, 58, 58, 60, 61]

fat = [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2, 34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]

data = pd.DataFrame({'Age': age, '%Fat': fat})

age_mean = data['Age'].mean()

age_median = data['Age'].median()

age_std = data['Age'].std()

fat_mean = data['%Fat'].mean()

fat_median = data['%Fat'].median()

fat_std = data['%Fat'].std()

print("Age Statistics:")

print(f"Mean: {age_mean}, Median: {age_median}, Standard Deviation: {age_std}")

print("\n%Fat Statistics:")

print(f"Mean: {fat_mean}, Median: {fat_median}, Standard Deviation: {fat_std}")

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)

sns.boxplot(y=data['Age'])

plt.title('Boxplot of Age')

plt.subplot(1, 2, 2)

sns.boxplot(y=data['%Fat'])

plt.title('Boxplot of %Fat')

plt.tight_layout()

plt.show()

plt.figure(figsize=(6, 6))

sns.scatterplot(x=data['Age'], y=data['%Fat'])

plt.title('Scatter Plot of Age vs %Fat')

plt.xlabel('Age')

plt.ylabel('%Fat')

plt.show()

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)

stats.probplot(data['Age'], dist="norm", plot=plt)

plt.title('Q-Q Plot for Age')

plt.subplot(1, 2, 2)

stats.probplot(data['%Fat'], dist="norm", plot=plt)

plt.title('Q-Q Plot for %Fat')

plt.tight_layout()

plt.show()
