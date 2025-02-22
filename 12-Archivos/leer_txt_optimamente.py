# Abriendo el archivo with open
with open("12-Archivos\\prueba.txt", encoding="UTF-8") as archivo:
    # for linea in archivo:
        # print(linea)
    print(archivo.read()) # Lee todo el archivo
# No es necesario cerrar el archivo