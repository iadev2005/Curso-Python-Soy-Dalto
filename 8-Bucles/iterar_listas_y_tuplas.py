# El bucle for funciona tanto para tuplas como para listas

animales = ["gato", "perro", "loro", "cocodrilo"]
# Recorriendo lista animales
for animal in animales:
    print("Ahora la variable animal tiene el valor de: " + animal)
numeros= [10,62,12,72]

# Recorriendo lista numeros
for numero in numeros: 
    resultado = numero * 10
    print(resultado)

# Bucle simultáneo (mismo tamaño)
for numero,animal in zip(numeros,animales):
    print("El animal es: " + animal + " y el numero es: " + str(numero))

# Funcion range (El primero incluido el último no)
for num in range(5,10):
    print(num)

# Si le ponemos un solo parámetro arranca de 0 hasta el parámetro
for num in range(10):
    print(num)  # Imprime del 0 al 9

# Una manera muy interesante es la siguiente (no óptima)
for num in range(len(animales)):
    print(animales[num])

# Forma correcta de recorrer una lista con su índice enumerate
for num in enumerate(animales):
    print(num) # Nos devuelve una tupla con el índice y el valor
    print(num[0]) # Imprime el índice
    print(num[1]) # Imprime el valor

# Podemos desempaquetar la tupla en el for
for num, i in enumerate(numeros):
    print(num) # num va poniendo el índice de la tupla
    print(i) # i va desempaquetando la tupla

# Usando el else
for num in numeros:
    print(f"Ejecutando el ultimo bucles, valor actual: {num}")
else:
    print("Fin de la lista") 

#Con tuplas (funciona excatamente igual)
tupla= (2,3,4)
for t in tupla: 
    print(t)  