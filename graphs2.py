# Importar librerias utiles para la manipulacion y visualizacion de data
import matplotlib.pyplot as plt
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Importar datos de archivo train.csv
train = pd.read_csv('train.csv')
figsize_rect = (12, 7)  # dimensiones para graficos en formato rectangular
figsize_sqr = (9, 9)  # dimensiones para graficos en formato cuadrado

# 3.7. Realice una gráfica de pastel y una gráfica de barras para cualquier variable categórica (libre elección).
plt.figure(figsize=figsize_sqr)
frequencyToMszoning = train.groupby('MSZoning')['MSZoning'].count()
frequencyToMszoning.plot(kind='pie', autopct='%1.f%%')
plt.draw()

plt.figure(figsize=figsize_rect)
frequencyToMszoning.plot(kind='bar')
plt.ylabel("Frequency")
plt.draw()

# 3.8. Realice una gráfica de pastel y una gráfica de barras para cualquier variable cuantitativa (libre elección).
plt.figure(figsize=figsize_sqr)
frequencyToFireplaces = train.groupby('Fireplaces')['Fireplaces'].count()
frequencyToFireplaces.plot(kind='pie', autopct='%1.f%%')
plt.draw()

plt.figure(figsize=figsize_rect)
frequencyToFireplaces.plot(kind='bar')
plt.ylabel("Frequency")
plt.draw()

# 3.9. Realice gráficas de línea y unas gráficas de puntos para dos variables cuantitativas (libre elección).
plt.figure(figsize=figsize_rect)
yearToPrice = train.loc[train['YearBuilt'] >= 1920].groupby('YearBuilt')['SalePrice'].agg(np.mean)
yearToPrice.plot.line(color="#46a5e5", figsize=figsize_rect)
plt.xlabel('Year built')
plt.ylabel('Sale price')
plt.draw()

yearToPrice.rename_axis(
    'YearBuilt').reset_index(name='SalePrice').plot.scatter(x='YearBuilt', y='SalePrice', color="#46a5e5",
                                                            figsize=figsize_rect)
plt.xlabel('Year built')
plt.ylabel('Sale price')
plt.draw()

frequencyToRooms = train.groupby('TotRmsAbvGrd').size().rename_axis('TotRmsAbvGrd').reset_index(name='Frequency')
frequencyToRooms.plot.line(color="#46a5e5", x='TotRmsAbvGrd', y='Frequency', figsize=figsize_rect)
plt.ylabel("Frequency")
plt.xlabel("TotRmsAbvGrd")
plt.draw()

frequencyToRooms.plot.scatter(x='TotRmsAbvGrd', y='Frequency', figsize=figsize_rect)
plt.ylabel("Frequency")
plt.xlabel("TotRmsAbvGrd")
plt.draw()

# 3.10. Realice un histograma de frecuencia relativa para cualquiera de las variables.
plt.figure(figsize=figsize_rect)
plt.hist(train.SalePrice, bins=20, color='#02b6f2', rwidth=0.9)
plt.xlabel("Sale Price")
plt.ylabel("Frequency")
plt.draw()

plt.show()  # Mostrar graficos
