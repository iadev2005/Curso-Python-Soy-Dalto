# Creando una lista
lista = ["Ignacio Aliendres", "iadev2005", True, 1.75]
print(lista) # Imprime todos los datos de la lista
print(lista[0]) # Imprime el primer elemento de la lista (mi nombre)

# La diferencia con las listas, es que las tuplas no se pueden modificar
tupla = ("Ignacio Aliendres", "iadev2005", True, 1.75) # Creación de la tupla
print(tupla[0])

lista[3]= "Maquina"
print(lista[3])

# Esto no se puede hacer
# tupla[3]= "cambio"
# print(tupla[3])

# Conjunto o Set
# No tienen un orden fijo, son elementos desordenados y pueden cambiar
conjunto= {"Ignacio Aliendres", "iadev2005", True, 1.75}

# El conjunto se puede modificar, pero los elementos no
# conjunto[1]= "Pedro" Esto no se puede hacer

# Sin embargo se puede redifinir
conjunto= {"Mala mia bro"}

# Esto también se puede hacer con las tuplas
tupla= {"Mala mia bro x2"}

# A diferencia de las listas en los conjuntos no se puede acceder a un elemento por el índice
# print(conjunto[1]) No se puede hacer esto

# Tampoco deja repetir valores (no se pueden poner datos duplicados en conjuntos)
# conjunto= {"Ignacio Aliendres"}

# Creando un diccionario (muestra por valor asociado 'key' : value)
diccionario= {
    'nombre' : "Ignacio Aliendres",
    'canal' : "iadev2005",
    'emocionado' : True,
    'altura' : 1.84,
    'dato-duplicado' : "Ignacio Aliendres"
}

# Comparación con lista:
#diccionario= {
    # 1 : "Ignacio Aliendres",
    # 2 : "iadev2005",
    # 3 : True,
    # 4 : 1.84,
    # 5 : "Ignacio Aliendres"
#}

print(diccionario['canal'])