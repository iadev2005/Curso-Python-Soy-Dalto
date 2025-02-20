# Creando diccionarios con dict()
diccionario = dict(nombre="Ignacio", apellido="Aliendres")
# NOTA: para crear un diccionario vacio basta con dict()

# Las listas no pueden ser claves
# diccionario = {["ignacio","rancio"]:"jsjsjs"}

# Las tuplas si pueden ser claves
diccionario = {("ignacio","rancio"):"jsjsjs"}

print(diccionario)

# Podemos usar frozenset para meter conjuntos
diccionario = {frozenset(["ignacio", "rancio"]):"jsjsjs"}

print(diccionario)

# Creando diccionarios con fromkeys()
diccionario = dict.fromkeys(["nombre", "apellido"])
print(diccionario)
print(diccionario["apellido"])

# Esto va iterando sobre el primer parametro y va asociando con el segundo
diccionario = dict.fromkeys("ABCDE", "VALOR2")
print(diccionario)

# Podemos dar una lista en el primer parámetro y dar un valor definido para cada elemento de la lista en el segundo
diccionario = dict.fromkeys(["nombre", "apellido"], "No se")
print(diccionario)