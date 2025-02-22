# Promedio de duración
otros_cursos_min = 2.5
otros_cursos_max = 7
otros_cursos_promedio = 4
dalto_curso = 1.5

# Duración de crudos (vídeos sin editar)
crudo_promedio = 5
crudo_dalto = 3.5

# Diferencias de duración
diferencia_min = 100 - round((dalto_curso / otros_cursos_min * 100),2) 
diferencia_max = 100 - round((dalto_curso / otros_cursos_max * 100),2)
diferencia_promedio = 100 - round((dalto_curso / otros_cursos_promedio * 100),2)

# Calculando el porcentaje de tiempo vacío
tiempo_vacio_promedio = 100 - round((otros_cursos_promedio / crudo_promedio * 100),2)
# tiempo_vacio_dalto = 100 - dalto_curso * 1000 // crudo_dalto / 10
tiempo_vacio_dalto = 100 - round((dalto_curso / crudo_dalto * 100),2)

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
equivalencia_este_curso_con_otros = round((otros_cursos_promedio / dalto_curso * 10),2)
print(f"Ver 10 horas de este curso equivale a ver {equivalencia_este_curso_con_otros} horas de otros cursos")
equivalencia_otro_curso_con_este_curso= round((dalto_curso / otros_cursos_promedio * 10),2)
print(f"Ver 10 horas de otros cursos equivale a ver {equivalencia_otro_curso_con_este_curso} horas de este curso")
print("-----------------------------------------")
