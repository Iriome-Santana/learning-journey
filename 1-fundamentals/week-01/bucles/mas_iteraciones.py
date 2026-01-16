frutas = ["manzana", "pera", "platano", "uva", "mango", "granada", "ciruelas"]
cadena = "Hola Iriome"
numeros = [2, 5, 8, 10]
"""evitando que se coma una manzana con continue (ignorar elemento en un for in)"""
for fruta in frutas:
    if fruta == "manzana":
        continue
    print(f"Me voy a comer un/a {fruta}")

"""evitando que se coma mas frutas despues de un platano con break (parar el bucle cuando llega a un elemento especifico)"""
for fruta in frutas:
    print(f"Me voy a comer un/a {fruta}")
    if fruta == "platano":
        break
print("Bucle terminado")

"""Recorrer cadena de texto"""

for letra in cadena:
    print(letra)

"""for en una sola linea de codigo para numeros(duplicamos los numeros)"""
numeros_duplicados = [x*2 for x in numeros]
print(numeros_duplicados)