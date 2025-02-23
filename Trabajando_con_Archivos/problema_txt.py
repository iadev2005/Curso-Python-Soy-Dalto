# Tenemos dos lista con nombre y apellido
# Queremos escribirlo en un .txt con un for
nombres = ["Juan", "Pedro", "Luis"]
apellidos = ["Perez", "Gomez", "Gonzalez"]

# Registrar esta información en un TXT de forma óptima

with open("Trabajando_con_Archivos\\nombres_y_apellidos.txt", "w") as arch: 
    arch.writelines("Los datos son:\n")
    [arch.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n") for n, a in zip(nombres, apellidos)]

# La instrucción es equivalente a:
# for n, a in zip(nombres, apellidos):
    # arch.writelines(f"Nombre: {n}\nApellido: {a}\n-----------\n")