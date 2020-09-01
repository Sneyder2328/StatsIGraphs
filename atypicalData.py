# Importar librerias utiles para la manipulacion y visualizacion de data
import matplotlib.pyplot as plt
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)
import seaborn as sns

# Importar datos de archivo train.csv
train = pd.read_csv('train.csv', index_col='Id')


# print(train)

# 3.11. Detectar mediciones atípicas en los datos.
def get_outliers(attr):
    list_data = sorted(train[attr].tolist())
    Q1, Q3 = np.quantile(list_data, [0.25, 0.75])
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    # print(Q1, Q3, IQR, lower_bound, upper_bound)
    return [num for num in list_data if num < lower_bound or num > upper_bound]


print(get_outliers('GarageArea'))  # Mediciones atipicas en la variable GarageArea
print(get_outliers('LotArea'))  # Mediciones atipicas en la variable LotArea

list1 = train.groupby('LotArea').size().reset_index(name='Frequency')
list1.plot.line(color="#46a5e5", x='LotArea', y='Frequency')
plt.show()
