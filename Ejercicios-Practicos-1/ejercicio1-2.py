frase = input("Decime una frase y te calculo cuando tardarias si tuvieras que decirlo: ")
palabras_separadas = frase.split(" ")
cantidad_de_palabrass = len(palabras_separadas)
print(f"Dijiste {cantidad_de_palabrass} palabras, y tardarias {cantidad_de_palabrass/2} segundos en decirlo")
print(f"Dalto lo diria en {(cantidad_de_palabrass/2)*1.3} segundos en decirlo")

if(cantidad_de_palabrass > 120) :
    print("Para flaco eso es una banda")