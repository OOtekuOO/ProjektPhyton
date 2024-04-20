import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = sns.load_dataset('mpg')


print("Pierwsze wiersze danych:")
print(df.head())


print("\nPodstawowe statystyki:")
print(df.describe())


print("\nIloœæ wartoœci null w danych:")
print(df.isnull().sum())


df.fillna(df.mean(), inplace=True)


plt.figure(figsize=(10, 6))

plt.subplot(2, 2, 1)
sns.histplot(df['mpg'], kde=True)
plt.title('Histogram MPG')


plt.subplot(2, 2, 2)
sns.scatterplot(data=df, x='horsepower', y='mpg')
plt.title('Wykres punktowy MPG vs Horsepower')


plt.subplot(2, 2, 3)
sns.boxplot(data=df, y='horsepower')
plt.title('Boxplot dla Horsepower')


plt.subplot(2, 2, 4)
sns.kdeplot(data=df, x='mpg', hue='origin', fill=True, common_norm=False)
plt.title('Rozk³ad MPG dla ró¿nych krajów pochodzenia')

plt.tight_layout()
plt.show()


