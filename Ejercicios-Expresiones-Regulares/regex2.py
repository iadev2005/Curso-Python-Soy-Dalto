import re
 # La cadena en la que se buscarán patrones
text = "La fecha es 13/06/2021 y el telefono es +1-555-555-5555"

# El patrón a buscar
patron = r"\d{2}/\d{2}/\d{4}"

# El texto con el que se reemplazará el patrón
reemplazo= "Fecha oculta"

# Reemplazar todas las aparaciones del patrón en la cadena de texto
new_text = re.sub(patron, reemplazo,text)

print("Texto modificado: ", new_text)