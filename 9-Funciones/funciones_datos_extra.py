def frase(nombre,apellido,adjetivo):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

# Utilizando keywords arguments
frase_resultante = frase(adjetivo="capo", apellido="Aliendres", nombre="Ignacio")
print(frase_resultante)

# No hace falta pasar ese argumento, si se pasa cuando se llama la función se cambia
def frase(nombre,apellido,adjetivo="fuerte"):
    return f"Hola {nombre} {apellido}, sos muy {adjetivo}"

frase_resultante = frase("Ignacio", "Aliendres")
print(frase_resultante)

frase_resultante = frase("Ignacio", "Aliendres", "inteligente")
print(frase_resultante)