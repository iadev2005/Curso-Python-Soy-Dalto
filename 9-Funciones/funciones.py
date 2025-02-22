# Encontrando el numero mayor de una lista
numeros = (4,7,1,42,15)
numero_mas_alto = max(numeros)
print(numero_mas_alto)

# Encontrando el número menor de una lista
numero_mas_bajo = min(numeros)
print(numero_mas_bajo)

# Redondeando a 6 decimales
# Eñ segundo parámetro determina cuantos decimales se guardaran
numero = round(12.345678, 2)
print(numero)

# Retorna false si le pasamos 0, vacio, false o ninguno(none). True si todo lo contrario
resultado_bool = bool(0)
print(resultado_bool)

# Retorna True si todos los valores son verdaderos
resultado_all = all([234,"true",[344,23]])
# resultado_all = all([0,"true",[344,23]]) # Con esto devolvería False
print(resultado_all)

# Suma todos los valores de un iterable (tienen que ser números)
suma_total = sum(numeros)
print(suma_total)