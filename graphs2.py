import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

train = pd.read_csv('train.csv')


# 3.7. Realice una gráfica de pastel y una gráfica de barras para cualquier variable categórica (libre elección).
plt.figure(1)
frequencyToMszoning = train.groupby('MSZoning')['MSZoning'].count()
frequencyToMszoning.plot(kind='pie', autopct=('%1.f%%'))
plt.draw()

plt.figure(2)
frequencyToMszoning.plot(kind='bar')
plt.ylabel("Frequency")
plt.draw()


# 3.8. Realice una gráfica de pastel y una gráfica de barras para cualquier variable cuantitativa (libre elección).
plt.figure(3)
frequencyToFireplaces = train.groupby('Fireplaces')['Fireplaces'].count()
frequencyToFireplaces.plot(kind='pie', autopct=('%1.f%%'))
plt.draw()

plt.figure(4)
frequencyToFireplaces.plot(kind='bar')
plt.ylabel("Frequency")
plt.draw()


# 3.9. Realice gráficas de línea y unas gráficas de puntos para dos variables cuantitativas (libre elección).
plt.figure(5)
yearToPrice = train.loc[train['YearBuilt'] >= 1920].groupby('YearBuilt')['SalePrice'].agg(np.mean)
yearToPrice.plot.line(color="#46a5e5")
plt.xlabel('Year built')
plt.ylabel('Sale price')
plt.draw()

yearToPrice.rename_axis(
    'YearBuilt').reset_index(name='SalePrice').plot.scatter(x='YearBuilt', y='SalePrice', color="#46a5e5")
plt.xlabel('Year built')
plt.ylabel('Sale price')
plt.draw()

frequencyToRooms = train.groupby('TotRmsAbvGrd').size().rename_axis('TotRmsAbvGrd').reset_index(name='Frequency')
frequencyToRooms.plot.line(color="#46a5e5", x='TotRmsAbvGrd', y='Frequency')
plt.ylabel("Frequency")
plt.xlabel("TotRmsAbvGrd")
plt.draw()

frequencyToRooms.plot.scatter(x='TotRmsAbvGrd', y='Frequency')
plt.ylabel("Frequency")
plt.xlabel("TotRmsAbvGrd")
plt.draw()

# 3.10. Realice un histograma de frecuencia relativa para cualquiera de las variables.
plt.figure(9)
plt.hist(train.SalePrice, bins=20, color='#02b6f2', rwidth=0.9)
plt.xlabel("Sale Price")
plt.ylabel("Frequency")
plt.draw()


plt.show()
