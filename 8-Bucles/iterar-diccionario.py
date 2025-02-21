diccionario = {
    "nombre" : "Ignacio",
    "apellido" : "Aliendres",
    "edad" : 19
}

print(diccionario)

# Para solamente las claves
for key in diccionario:
    print(key)

# Para mostrar el elemento (devuelve tupla clave-valor)
for key,i in diccionario.items():
    print(key) # El campo
    print(i) # El valor del campo


    
