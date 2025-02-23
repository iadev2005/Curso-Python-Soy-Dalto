import re
email = "example@example.com"
patron = "[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
resultado = re.match(patron,email)
if resultado:
    print("Dirección de correo valida")
else:
    print("Dirección de correo no valida")
