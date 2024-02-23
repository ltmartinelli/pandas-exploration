import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

# Setup DataFrame and Options

df = pd.read_csv(r'world_population.csv')
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.set_option('display.width', 1000)
pd.set_option('display.max_columns', 500)

# Useful methods

#INFO
print(df.info())

#DESCRIBE
print(df.describe())

#ISNULL and SUM
print(df.isnull().sum())

#NUNIQUE
print(df.nunique())

#SORT_VALUES AND HEAD
print(df.sort_values(by='World Population Percentage', ascending=False).head(10))

#CORR AND HEATMAP(How closely correlated columns are)

plt.rcParams['figure.figsize'] = (20,7)
sns.heatmap(df.corr(numeric_only=True), annot = True)
plt.show()

#GROUPBY

print(df.groupby('Continent').mean(numeric_only=True).sort_values(by="2022 Population",ascending=False))

df2 = df.groupby('Continent')[['1970 Population',
       '1980 Population', '1990 Population', '2000 Population',
       '2010 Population', '2015 Population', '2020 Population',
       '2022 Population']].mean(numeric_only=True).sort_values(by="2022 Population",ascending=False)
df3 = df2.transpose()
df3.plot()
plt.show()