import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

train = pd.read_csv('train.csv')
# train.info()
# train.corr()

# train.groupby('GarageCars').size().plot.line()
# train.sort_values('PoolArea').plot(x='PoolArea', y='SalePrice', kind='line')
# train.sort_values('TotRmsAbvGrd').plot(x='TotRmsAbvGrd', y='SalePrice', kind='line')
# train.sort_values('FullBath').plot(x='FullBath', y='SalePrice', kind='line')
# train.sort_values('GrLivArea').plot(x='GrLivArea', y='SalePrice', kind='line')
# train.sort_values('1stFlrSF').plot(x='1stFlrSF', y='SalePrice', kind='line')
# train.sort_values('TotalBsmtSF').plot(x='TotalBsmtSF', y='SalePrice', kind='line')
# train.sort_values('GarageArea').plot(x='GarageArea', y='SalePrice', kind='line')

# 3.7. Realice una gráfica de pastel y una gráfica de barras para cualquier variable categórica (libre elección).

# labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
# sizes = [15, 30, 45, 10]
# plt.pie(train.HouseStyle, autopct='%1.1f%%', shadow=False, startangle=90)
# plt.axis('equal')
# plt.show()
plt.figure(1)
train.groupby('MSZoning')['MSZoning'].count().plot(kind='pie', autopct=('%1.f%%'))
plt.draw()

plt.figure(2)
train.groupby('MSZoning')['MSZoning'].count().plot(kind='bar')
plt.ylabel("Frequency")
plt.draw()

# plot2 = plt.figure(2)
# train.groupby('MSZoning')['MSZoning'].count().plot(kind='pie', autopct=('%1.f%%'))
# legend = (
# 'C Commercial', 'FV  Floating Village Residential', 'RH  Residential High Density', 'RL  Residential Low Density',
# 'RM Residential Medium Density')
# plt.xlabel('Frecuencia')
# plt.title('Gráfica de la clasificación de las zonas de las ventas (MSZoning)')
# plt.legend(labels=legend)
# plt.show()


# 3.8. Realice una gráfica de pastel y una gráfica de barras para cualquier variable cuantitativa (libre elección).

plt.figure(3)
train.groupby('Fireplaces')['Fireplaces'].count().plot(kind='pie', autopct=('%1.f%%'))
plt.draw()

plt.figure(4)
train.groupby('Fireplaces')['Fireplaces'].count().plot(kind='bar')
plt.ylabel("Frequency")
plt.draw()

# 3.9. Realice gráficas de línea y unas gráficas de puntos para dos variables cuantitativas (libre elección).

# train.sort_values('YearBuilt').plot(x='YearBuilt', y='SalePrice', kind='line')
# print(train.loc[(train['YearBuilt'] >= 1920)].sort_values('YearBuilt').loc[:, ['YearBuilt', 'SalePrice']])
years = [year for year in sorted(train.YearBuilt.unique().tolist()) if year >= 1920]
print(years)
# years = train.loc[(train['YearBuilt'] >= 1920)].sort_values('YearBuilt').YearBuilt.unique().tolist()
prices = [train.loc[train['YearBuilt'] == year].SalePrice.mean() for year in years]
print(prices)
plt.figure(5)
plt.plot(years, prices, color="#46a5e5")
plt.xlabel('Year built')
plt.ylabel('Sale price')
plt.draw()

plt.figure(6)
plt.plot(years, prices, 'ro', markersize=4, color="#46a5e5")
plt.xlabel('Year built')
plt.ylabel('Sale price')
plt.draw()

plt.figure(11)
print(train.loc[train['YearBuilt'] >= 1920].groupby('YearBuilt')['SalePrice'].agg(np.mean))
train.loc[train['YearBuilt'] >= 1920].groupby('YearBuilt')['SalePrice'].agg(np.mean).plot.line(color="#46a5e5")

# plt.plot(years, prices, 'ro', markersize=4, color="#46a5e5")
# plt.xlabel('Year built')
# plt.ylabel('Sale price')
plt.draw()


df = train.groupby('TotRmsAbvGrd').size().rename_axis('TotRmsAbvGrd').reset_index(name='frequency')
df.plot.line(color="#46a5e5", x='TotRmsAbvGrd', y='frequency')
plt.ylabel("Frequency")
plt.xlabel("TotRmsAbvGrd")
plt.draw()
# print(df)

df.plot.scatter(x='TotRmsAbvGrd', y='frequency')
plt.ylabel("Frequency")
plt.draw()

# 3.10. Realice un histograma de frecuencia relativa para cualquiera de las variables.
plt.figure(9)
plt.hist(train.SalePrice, bins=20, color='#02b6f2', rwidth=0.9)
plt.xlabel("Sale Price")
plt.ylabel("Frequency")
plt.draw()

plt.show()