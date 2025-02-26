# list crea una lista
# Un buen uso, es para crear una lista vacía
lista= list(["Hola", "Ignacio", 19])
print(lista)

# len() devuelve la cantidad de elementos de una lista
cnt_elementos = len(lista); 
print(cnt_elementos)

# append() agrega un elemento al final de la lista
agregando_con_append = lista.append("Nacho")
print(lista)

# insert() agrega un elemento en una posición específica
lista.insert(2, "Toma Mama")
print(lista)

# extend() agrega varios elementos al final de la lista
lista.extend(["elpapu", 49]) # Le tenemos que pasar otra lista
print(lista)

# pop() elimina un elemento de la lista por su índice
print(len(lista)) # Tiene 7 elementos
lista.pop(0) 
print(lista)
print(len(lista)) # Se reduce a 6 elementos

# Una técnica para eliminar el último elemento es
lista.pop(-1) # -2 nos eliminaría el penúltimo y así sucesivamente
print(lista)

# remove() elimina un elemento de la lista por su valor
lista.remove("Ignacio")
print(lista) # Si le pasamos un parámetro que no encuentra lanza una exepción

# sort() ordena los elementos de la lista de forma ascendente si reverse= True lo ordena en forma descendente
# pero no sirve si la lista tiene cadenas de texto
lista2 = [1, 5, 3, 2, 4]
lista2.sort() # 1, 2, 3, 4, 5
# lista2.sort(reverse=True) # 5, 4, 3, 2, 1
print(lista2)

# reverse() invierte los elementos de la lista (sin orden específico, solo invierte)
lista2.reverse()
print(lista2)

# index() devuelve el índice de un elemento de la lista
elemento_encontrado = lista2.index(4)
print(elemento_encontrado) # lo encontro en la posición 1

# En las tuplas solo podemos buscar elementos y contarlos
# ya que las tuplas son inmutables

# clear() elimina todos los elementos de la lista
lista.clear()
print(lista) # Lista vacía