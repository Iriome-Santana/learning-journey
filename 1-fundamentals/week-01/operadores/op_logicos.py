#AND si ambas condiciones son verdaderas devuelve True
Resultado = True and True #Devuelve True si 
Resultado1 = True and False #Devuelve False
Resultado2 = False and True #Devuelve False
Resultado3 = False and False #Devuelve False

#OR si alguna de las condiciones es verdadera devuelve True
Resultado4 = True or True #Devuelve True
Resultado5 = True or False #Devuelve True
Resultado6 = False or True #Devuelve True
Resultado7 = False or False #Devuelve False 

#NOT
Resultado8 = not True #Devuelve False
Resultado9 = not False #Devuelve True


edad = 18
tiene_licencia = True

es_mayor_de_edad = edad >= 18   
puede_ingresar_a_un_bar = es_mayor_de_edad and tiene_licencia

print(puede_ingresar_a_un_bar)




#print(Resultado7)