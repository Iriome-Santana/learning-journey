cadena1 = "Hola,soy,Iriome"
cadena2 = "Bienvenido a Python"

#coversion a mayusculas
mayusc = cadena2.upper()

#conversion a minusculas
minusc = cadena2.lower()

#solo primera letra mayuscula
primera_mayusc = cadena2.capitalize()

#buscamos una cadena en otra cadena, si no la encuentra devuelve -1
busqueda_find = cadena2.find("a")

#buscamos una cadena en otra cadena, si no la encuentra devuelve una excepcion
busqueda_index = cadena2.index("Python")

#si es numerico devolvemos true (solo en string)
es_numerico = cadena1.isnumeric()

#si es alfanumerico devolvemos true (solo en string) sin contar espacios
es_alfanumerico = cadena1.isalpha()

#contar coincidencias en una cadena
coincidencias = cadena1.count("o")

#contamos cuantos caracterres tiene la cadena
longitud_cadena = len(cadena1)

#verificamos si una cadena empieza con otra cadena dada, si es asi devuelve true
empieza_con = cadena1.startswith("O")

#verificamos si una cadena termina con otra cadena dada, si es asi devuelve true
termina_con = cadena1.endswith("e")    

#Reemplazamos una subcadena por otra
cadena_nueva = cadena1.replace("o","a")

#separa una cadena en una lista de subcadenas
lista_cadenas = cadena1.split(",")


print(lista_cadenas)