# Importar librerias utiles para la manipulacion y visualizacion de data
import matplotlib.pyplot as plt
import numpy as np  # linear algebra
import pandas as pd  # data processing, CSV file I/O (e.g. pd.read_csv)

# Importar datos de archivo train.csv
train = pd.read_csv('train.csv')

# 3.11. Detectar mediciones atípicas en los datos.
