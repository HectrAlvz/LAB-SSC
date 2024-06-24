import pandas as pd
import re

# Leer el archivo de texto
with open('others/donQuijote/ElQuijote.txt', 'r', encoding='utf-8') as file:
    texto = file.read().replace('\n', ' ')

# Hacer minúsculas el texto
texto = texto.lower()

# Separar el texto en capítulos
capitulos = re.split('(?i)capítulo \d+', texto)

# Crear un DataFrame a partir de la lista de capítulos
df = pd.DataFrame(capitulos, columns=['Capitulo'])

# Imprimir el DataFrame
print(df)

# Guardar el DataFrame en un archivo CSV
df.to_csv('Capitulo 1 - Clasificacion de Texto/donQuijote/ElQuijote.csv', index=False)