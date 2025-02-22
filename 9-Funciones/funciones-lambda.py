# Lambda es una especie de función anónima, ya que no tiene nombre
multiplicar_por_dos = lambda x : x * 2
print(multiplicar_por_dos(5))
# La sección después del ":" se le puede considerar el cuerpo de la función
# Normalmente se usa para cosas cortas

# Usando filter con una función común
# Sirve para usar una función true o false, para crear una lista solo con los valores true
numeros = [1,2,3,4,5,6,7,8,9]
def es_par(n):
    if(n%2==0):
        return True
# Si el numero es par los va agregando
n_pares = filter(es_par,numeros)
print(list(n_pares))

# Creando lo mismo de antes pero con la función lambda
n_pares = filter(lambda n:n%2==0,numeros)
print(f"Con funcion lambda {list(n_pares)}")