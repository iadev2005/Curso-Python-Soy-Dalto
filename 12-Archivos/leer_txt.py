archivo_sin_leer = open("12-Archivos\\prueba.txt", encoding="UTF-8")
# Leer archivo completo
# archivo = archivo_sin_leer.read()
# Para guardar las lineas en una lista
# lineas = archivo_sin_leer.readlines()
# print(archivo)
# \n es el salto de línea
# Antes tenemos que cerrarlo
# Leer una sola línea
# Lo que se ponga dentro del parentesís representará el número de caracteres que se leerán
linea = archivo_sin_leer.readline()
print(linea)

# cerrar el archivo
archivo_sin_leer.close()
# Una vez cerrado no se puede leer