import csv
with open("12-Archivos\\datos.csv") as archivo:
    # print("Datos leidos correctamente")
    reader= csv.reader(archivo)
    for row in reader:
        print(row)
