animales = ["perro", "gatos", "loros"]
numeros = [15, 324, 40]

for animal in animales:
    print(animal)
    
"""ecorriendo la lista numeros y multiplicandolos por dos"""

"""for numero in numeros:
    resultado = numero*2
    print(resultado)"""""
    
"""Iterando listas del mismo tamaño al mismo tiempo"""
for numero, animal in zip(numeros, animales):
    print(f"Recorriendo lista 1: {numero}")
    print(f"Recorriendo lista 2: {animal}")
    print(f"numero y animal: {numero} - {animal}")


"""forma optima de recorrer una lista con su indice"""
for num in enumerate(numeros):
    indice = num[0]
    valor = num[1]
    print(f"El indice es: {indice} y el valor es: {valor}")

"""usando el else"""
for num in numeros:
    print(f"Ejecutando el bucle por el numero: {num}")
    
else:
    print("El bucle terminó")
    
""" TODO LO ANTERIOR FUNCIONA IGUAL PARA TUPLAS Y CONJUNTOS"""