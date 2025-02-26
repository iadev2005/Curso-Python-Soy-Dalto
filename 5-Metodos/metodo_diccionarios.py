diccionario = {
    "nombre" : 'Ignacio',
    "apellido" : 'Aliendres',
    "edad" : 19
}

# keys() devuelve las claves del diccionario
# También nos sirve para iterar
claves = diccionario.keys()
print(claves)

# Las claves también nos sirven para tener un Array (tupla) con todas las claves

claves = diccionario.get("nombre")
print(claves) # Nos muestra el nombre

# También se puede hacer esto:
# diccionario = {
#     0 : 'Ignacio',
#     1 : 'Aliendres',
#     2 : 19
# }

# claves = diccionario[0]

# Si le pasamos al get algo que no esta identificado lanza un None
# Es decir el programa continua

# pop() elimina un elemento del diccionario por su clave
diccionario.pop("nombre")
print(diccionario) # Eliminamos el nombre

# items() devuelve una lista de tuplas con clave y valor
diccionario_iterable = diccionario.items()
print(diccionario_iterable)

# clear() elimina todos los elementos del diccionario
diccionario.clear()
print(diccionario) # Diccionario vacío