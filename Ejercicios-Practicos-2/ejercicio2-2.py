# Función, números primos
# Mi solución
def esPrimo(n):
    for divisor in range(2,n-1):
        if n%divisor == 0:
            return False
    return True

def listaPrimos(n):
    primos=[]
    for i in range(1,n):
        if(esPrimo(i)):
            primos.append(i)
    return primos

# Con recursividad:
def listaPrimosRecursiva(n,i=1):
    primos=[]
    if(i<n):
        if(esPrimo(i)):
            primos.append(i)
        primos = primos + listaPrimosRecursiva(n,i+1)
        
    return primos

print(listaPrimosRecursiva(18))
    