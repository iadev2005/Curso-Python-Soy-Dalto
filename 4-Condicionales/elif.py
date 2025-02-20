# if anidados y else if (elif)

ingreso_mensual = 10000
gasto_mensual = 2000

if ingreso_mensual >= 1000000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estas en deficit")
    elif ingreso_mensual - gasto_mensual > 3000:
        print("Esta bien pa")
    else:
        print("Y bueno pa, estas gastando una banda, te toca laburar")
elif ingreso_mensual >= 10000:
    print("Estas bien en LATAM")
elif ingreso_mensual <= 500:
    print("Estas bien en Argentina")
elif ingreso_mensual <= 200:
    print("Estas bien en la Republica Democratica del Congo")
else:
    print("Sos pobre wachin")