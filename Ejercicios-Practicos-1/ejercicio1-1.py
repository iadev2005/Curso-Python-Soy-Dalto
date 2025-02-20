# Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# Duración de crudos (vídeos sin editar)
crudo_promedio = 5
crudo_dalto = 3.5

# Diferencias de duración
diferencia_min = 100 - dalto_curso / otros_cursos_min * 100
diferencia_max = 100 - dalto_curso * 1000 // otros_cursos_max / 10
diferencia_promedio = 100 - dalto_curso / otros_cursos_promedio * 100

# Calculando el porcentaje de tiempo vacío
tiempo_vacio_promedio = 100 - otros_cursos_promedio * 1000 // crudo_promedio / 10
tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10

# Mostrando las diferencias de duración (ejercicio A)
print(f"La diferencia minima de duracion es: {diferencia_min}%")
print(f"La diferencia maxima de duracion es: {diferencia_max}%")
print(f"La diferencia promedio de duracion es: {diferencia_promedio}%")
print("-----------------------------------------")

# Mostrando la cantidad de espacios vacios que se remueven (ejercicios B)
print(f"Un curso elimina un {tiempo_vacio_promedio}% de tiempo vacio")
print(f"Este curso elimino el {tiempo_vacio_dalto}% de tiempo vacio")
print("-----------------------------------------")


# Mostrando diferencias si los cursos durarán 10 horas
print(f"Ver 10 horas de este curso equivale a ver {otros_cursos_promedio * 100 // dalto_curso / 10} horas de otros cursos")
print(f"Ver 10 horas de otros cursos equivale a ver {dalto_curso * 100 // otros_cursos_promedio/10} horas de este curso")
print("-----------------------------------------")
