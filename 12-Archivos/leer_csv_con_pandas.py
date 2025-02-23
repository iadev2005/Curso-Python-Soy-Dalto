import pandas as pd
# Manera más simple
df = pd.read_csv("12-Archivos\\datos.csv")
df2 = pd.read_csv("12-Archivos\\datos.csv")
# Para redifinir los campos
# df = pd.read_csv("12-Archivos\\datos.csv", names=["name","listname","age"])
print(df)
# Obteniendo los datos de la columna nombre
print(df["nombre"])

cadena = "0123456789"
print(cadena[0:3]) # Imprime del 0 al 2 012

# Supongamos que queremos organizar la edad:
df_ordenado = df.sort_values("edad")
print(df_ordenado)

# Ordenando de forma descendente
df_orden_descendete = df.sort_values("edad", ascending=False)
print(df_orden_descendete)

# Supongamos que queremos concatenar los 2 dataframes
df_concatenado = pd.concat([df, df2])
print(df_concatenado)

# Accediendo a las primeras tres filas
primera_fila = df.head(3)
print(primera_fila)

# Accediendo a las últimas 3 filas con tail
ultima_fila = df.tail(3)
print(ultima_fila)

# Accediendo a la cantidad de filas y columnas con shape
filas_y_columnas_totales = df.shape
filas_totales = df.shape[0]
columnas_totales = df.shape[1]
# Otra opción es desempaquetando
# filas_totales, columnas_totales = df.shape
print(filas_y_columnas_totales) # Es una tupla
print(filas_totales)
print(columnas_totales)

# Obteniendo data estadística del dataframe
df_info = df.describe()
print(df_info)

# Accediendo a un elemento específico del dataframe con loc
elemento_especifico = df.loc[1, "nombre"] # Las filas tienen nombres e índices	
print(elemento_especifico)

# Accediendo a la fila 3 con loc
fila_3 = df.loc[2,:]

# Accediendo a la fila 3 con iloc
fila_3 = df.iloc[2,:]

# Accediendo a todas las filas de una columna
apellido = df.iloc[:,1]
print(apellido)

# Accediendo a filas con edad mayor que 30
mayores_30 = df.loc[df["edad"] > 30,:]
print(mayores_30)