frutas = ["banana", "manzana", "ciruela", "pera", "naranja", "granada", "durazno"]
cadena = "Hola Ignacio"
numeros = [1,4,3,5,2]
# Evitando que se coma la granada con continue
for fruta in frutas:
    if fruta == "granada":
        continue; # El bucle se salta ese elemento
    print(f"Me voy a comer una {fruta}")

# Detener el bucle (nota: el else no se ejecuta después de un break en un bucle)
for fruta in frutas:
    if fruta == "pera":
        print("Bucle terminado, no me gustan las peras")
        break
    print(f"Me voy a comer una {fruta}")

# Recorrer cadena de texto
for letra in cadena:
    print(letra)

# for para duplicar valor
# numeros_duplicados = list()
# for numero in numeros:
    # numeros_duplicados.append(numero*2)

# print(numeros_duplicados)

# for en una sola línea de código (tambien los ordena)
numeros_duplicados = {x*4 for x in numeros}
print(numeros_duplicados)
