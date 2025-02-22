# def suma(a,b):
    # return a+b

# Pero supongamos que queremos sumar más números
# La forma normal sería pasar una lista y en la función ejecutar un bucle o usar la función sum para retornar el valor
# Pero Python nos ofrece la siguiente alternativa

# Forma no óptima
def suma(lista):
    n_sumados = 0
    for numero in lista:
        n_sumados = n_sumados + numero
    return n_sumados

resultado = suma([6,3,2,5,7,3,1])
print(resultado)

# Pero podemos hacer que la cantidad de argumentos sea indefinida
# Si usamos esto debe estar al final
def sumaOptima(*n): # Esto hace que todos los parametros sean uno solo
    return sum(n)

resultado = sumaOptima(3,65,6,5,7,3)
print(resultado)

def sumaConNombre(nombre, *n):
    return f"{nombre}, la suma de tus numeros es: {sum(n)}"

# resultado= sumaConNombre("Ignacio", (2,4,5)) # Esto esta mal ya que interpreta el segundo parámetro como parte de una tupla
resultado= sumaConNombre("Ignacio", 2,4,5)
print(resultado)

# Otra foma óptima de sumar valores
# Lo bueno es que acá este parámetro no esta forzado a ser el último
def suma_total(numeros):
    print(*numeros)
    return sum([*numeros])

resultado=suma_total([3,45,6])
print(resultado)
