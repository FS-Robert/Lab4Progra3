# movies.py

import pandas as pd
import numpy as np

# 1. Cargar el dataset
df = pd.read_csv('movies_metadata.csv', low_memory=False)

# 2. Usar describe() para resumir la información del dataset
print("Resumen estadístico con describe():")
print(df.describe(include='all'))

# 3. Identificar los tipos de datos de cada columna utilizando dtypes
print("\nTipos de datos de cada columna:")
print(df.dtypes)



# 4. Mostrar los primeros y últimos registros
print("\nPrimeros 5 registros (head()):")
print(df.head())

print("\nÚltimos 5 registros (tail()):")
print(df.tail())

# 5. Ordenar los resultados para ver categorías destacadas
#ordenar por 'vote_average' para ver las películas mejor y peor valoradas
print("\nPelículas con mayor promedio de votos (vote_average):")
print(df.sort_values(by='vote_average', ascending=False)[['title', 'vote_average']].head(10))

print("\nPelículas con menor promedio de Calificacion (vote_average):")
print(df.sort_values(by='vote_average', ascending=True)[['title', 'vote_average']].head(10))

# 6. Seleccionar una columna y calcular media, mediana y desviación estándar
vote_avg = pd.to_numeric(df['vote_average'], errors='coerce')  # Convertir a numérico por si hay errores

media = np.mean(vote_avg)
mediana = np.median(vote_avg.dropna())
desviacion = np.std(vote_avg.dropna())

print("\nEstadísticas de la columna 'vote_average (Calificacion)':")
print(f"Media: {media}")
print(f"Mediana: {mediana}")
print(f"Desviación estándar: {desviacion}")
