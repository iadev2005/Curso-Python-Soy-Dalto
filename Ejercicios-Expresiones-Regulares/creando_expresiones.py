import re

# Detectando un CABA y ocultándolo
texto = "Hola Pedro, mi numero es: +54 11 4321-4321 +54 11 4321-4321"
patron = r'\+\d{2}\s\d{2}\s\d{4}-\d{4}'
reemplazo = re.sub(patron, "(Numero oculto)", texto)
print(reemplazo)
