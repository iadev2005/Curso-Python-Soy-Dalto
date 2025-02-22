
with open("12-Archivos\\prueba.txt", "w", encoding="UTF-8") as archivo:
    # Esto sobre-escribe el archivo
    # archivo.write("Jsjsjsjs te la recontra teclee\n")
    archivo.writelines(["Hola maestro\n", "Misericordia\n"])
    archivo.writelines(["Hola maestro\n", "Misericordia"])
    