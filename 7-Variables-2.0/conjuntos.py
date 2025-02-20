# Creando un conjunto con set
conjunto = set({"Dato 1", ("datoenlista1", "datoenlista2")})
print(conjunto)

# Qué podemos piner datos modificables en no modificables?
conjunto1 = ("dato1", "dato 2")
# conjunto2 = {conjunto, "dato3"} # Esto no se puede
# Pero si:
conjunto1 = frozenset(["dato 1", "dato 2"])
conjunto2 = {conjunto1, "dato3"}
print(conjunto)

# Teoria de conjuntos
conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

# Para verificar si un conjunto es un subconjunto de otro podemos:
resultado = conjunto2.issubset(conjunto1)
print(resultado)

# Otra opción es la siguiente
resultado = conjunto2 <= conjunto1
print(resultado)

# Verificando si es un superconjunto
resultado = conjunto2.issuperset(conjunto1)
print(resultado)

# Otra forma
resultado = conjunto2 > conjunto1
print(resultado)

# Verificar si hay un elemento en común
resultado = conjunto2.isdisjoint(conjunto1)
print(resultado) # Si hay un elemento que coincide es falso