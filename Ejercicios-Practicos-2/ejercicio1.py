# Hoy falto el profesor a clases y los chicos se organizaron para armar la suya propia
# Uno de los alumnos es el profesor
# Y el otro es el asistente
# A) Pedir el nombre y la edad de los compañeros que vinieron hoy a clase y ordenar los datos de menor a mayor (en base a la edad)
# B) Obligatoriamente el mayor de la clase es el profesor y el menor es el asistente, ¿Cuáles son sus nombres?

# Mi solución (con algunas cosas adicionales)
# def rellenar_datos(estudiante): 
    # estudiante["nombre"] = input("Introduzca el nombre del estudiante: ")
    # estudiante["edad"] = int(input("Introduzca la edad del estudiante: "))
    # return estudiante

# def pedir_datos():
    # while True:
        # print("Bienvenido al sistema de gestion de estudiantes")
        # opcion =  input("Desea agregar mas estudiante? (S/N)").lower()
        # if(opcion == "n"):
            # break
        # elif (opcion == "s"):
            # Llamamos a rellenar datos e incluimos a ese estudiante en la lista
            # nuevo_estudiante = {} # Diccionario vacío
            # estudiantes.append(rellenar_datos(nuevo_estudiante))
        # else:
            # print("Opcion invalida intente nuevamente")

# def mostrar_estudiantes(estudiantes):
    # print(f"Los datos de los estudiantes son: {estudiantes}")

# def buscar_estudiante(estudiantes, nombre_a_buscar):
    # for estudiante in estudiantes:
        # Recuerda que se usan ("") para entrar en la clave de un diccionario
        # if(estudiante.get("nombre")) == nombre_a_buscar:
            # return estudiante
    # return None

# Será conveniente usar el método sorted
# def organizar_edad(estudiantes):
    # return sorted(estudiantes, key=lambda estudiante: estudiante["edad"])

# def es_profesor(estudiantes):
    # return estudiantes[-1]

# def es_asistente(estudiantes):
    # return estudiantes[0]

# estudiantes= list() # Creamos una lista vacía
# pedir_datos()
# print(f"Buscando a Ignacio: {buscar_estudiante(estudiantes, 'Ignacio')}")
# estudiantes = organizar_edad(estudiantes)
# mostrar_estudiantes(estudiantes)
# print(f"El estudiante con los datos {es_profesor(estudiantes)} es el profesor")
# print(f"El estudiante con los datos {es_asistente(estudiantes)} es el asistente")

# Mi segundo intento de solución (Con ayuda de Dalto):
def pedirDatos(cantidad):
    # Definimos una lista (donde cada elemento será una tupla)
    estudiantes= []
    # Vamos pidiendo los campos
    for i in range(cantidad):
        nombre=input("Ingrese el nombre del estudiante: ")
        edad=int(input("Ingrese la edad del estudiante: "))    
        # Vamos empaquetando la tupla
        estudiante = (nombre,edad)
        # Metemos el nuevo elemento a la lista
        estudiantes.append(estudiante)
    # Organizando por la edad
    # Para esto usamos la función sort y le iremos pasando el dato de la edad en otra función lambda
    estudiantes.sort(key=lambda x:x[1])
    # Como la lista ya esta organizada, podemos devolver el profesor y el asistente
    profesor = estudiantes[-1]
    asistente = estudiantes[0]
    return profesor,asistente # Devolvemos una tupla

cnt = int(input("Ingrese la cantidad de alumnos: "))
profesor, asistente = pedirDatos(cnt)
print(f"El profesor es {profesor[0]} con una  edad {profesor[1]}")
print(f"El asistente es {asistente[0]} con una  edad {asistente[1]}")
