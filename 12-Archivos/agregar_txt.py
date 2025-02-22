
with open("12-Archivos\\prueba.txt", "a", encoding="UTF-8") as archivo:
    # Añane este texto (sin sobreescribir)
    # archivo.writelines(["\nJsjsjsj ra la recontra teccle"])
    for i in range(10):
        archivo.write(f"Esta es la línea {i}\n")