# Cambiar el tipo de dato de una columna
import pandas as pd 
df = pd.read_csv("Trabajando_con_Archivos\\datos.csv")
# Convertir a String los datos de una columna
# df["edad"]=df["edad"].astype(str)
# print(type(df["edad"][0]))
# Reemplazando valores 
df["apellido"].replace("Ignacio", "Master", inplace=True)
print(df["apellido"])

# Supongamos que hay datos que estan faltando en las filas
# Podemos elimnarlas usando lo siguiente
df = df.dropna() # Eliminamos filas con datos faltantes
print(df)

# Si quisieramos eliminar las columnas con datos faltantes
df = df.dropna(axis=1) # Eliminamos columnas con datos faltantes
print(df)

# Supongamos que tengamos dos filas iguales
df = df.drop_duplicates()
print(df)

# Creando un CSB con el dataframe resultante (limpio)
df.to_csv("Trabajando_con_Archivos\\datos_limpio.csv")