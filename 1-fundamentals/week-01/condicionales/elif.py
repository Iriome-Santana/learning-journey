ingreso_mensual = 11000
gasto_mensual = 11000

#if anidado y else if (elif)

if ingreso_mensual >= 10000:
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en pérdida.")
    elif ingreso_mensual - gasto_mensual >= 3000:
        print("Estás bien.")
    else:
        print("Deberías controlar tus gastos.")
    
elif ingreso_mensual >= 5000:
    print("Eres una persona de ingresos altos en casi cualquier parte.") 
    if ingreso_mensual - gasto_mensual < 0:
        print("Estás en pérdida.")
    
elif ingreso_mensual >= 1000:
    print("Eres una persona de ingresos muy altos en latinoamerica.")   
    
elif ingreso_mensual >= 500:
    print("Eres una persona de ingresos altos en Argentina.")
    
elif ingreso_mensual >= 200:
    print("Eres una persona de ingresos altos en Venezuela.")
       
else:
    print("Eres una persona de ingresos bajos.")    