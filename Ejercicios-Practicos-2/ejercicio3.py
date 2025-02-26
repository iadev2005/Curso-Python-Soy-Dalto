# Serie de Fibonacci
def fibonacci(n):
    a,b = 0,1
    fibonacci_lista = []
    for i in range(n):
        if b >= n: return fibonacci_lista
        else: 
            fibonacci_lista.append(b)
            a,b=b,a+b
    return fibonacci_lista
print(fibonacci(20))