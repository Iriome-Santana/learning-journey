#creando una funcion simple

#def saludar():
    #print("Hola, ¿cómo estás?")
    
    
#ejecutando la funcion simple
#saludar()

#crear funcion que tenga parametros
nombre = input("Tu nombre: ")
sexo = input("Tu sexo: ")
edad = int(input("Introduce tu edad: "))

def saludar(nombre, sexo, edad):
    if sexo.lower() == "mujer":
        adjetivo = "maestra"
    elif sexo.lower() == "hombre":
        adjetivo = "maestro"
    else:
        adjetivo = "crack"
    if edad >= 18:
        print(f"Hola {nombre}, mi {adjetivo}, que tal, con {edad} años ya eres mayor de edad eh")
    else:
        print(f"Hola {nombre},mi {adjetivo} que tal, {edad} años tienes ya")
    
    
saludar(nombre, sexo,edad)

#crear una funcion que nos retorne valores

def crear_contraseña_random(num):
   chars = "abcdefghij"
   num_entero = str(num)
   num = int(num_entero[0])
   c1 = num - 2
   c2 = num
   c3 = num - 5
   contraseña = f"{chars[c1]}{chars[c2]}{chars[c3]}{num*2}"
   return contraseña, num
   
#desempaquetando la funcion
password, primer_num = crear_contraseña_random(7)

#mostrando la funcion
print(f"Tu contraseña es {password}")
print(f"El numero que usaste es {primer_num}")
   
   