"""Creando lista que se puede modificar(lista)"""
lista = ["Iriome", "Paola", 1.72, True]

#Creando lista que no se puede modificar (tupla)
tupla = ("Iriome", "Paola", 1.72, True)

"""Modificando un elemento de la lista(válido)
lista[3] = 180"""""

"""Accediendo a un elemento de la lista"""
print(lista[3])

"""Accediendo a un elemento de la tupla"""
print(tupla[0])

"""creando un conjunto(set) (no permite elementos repetidos, no se pueden llamar elementos por índice)"""
conjunto = {"Iriome", "Paola", 1.72, True}

""""creando un diccionario (dict) (la estructura es key :value y separados por comas)"""
diccionario = { 
      "nombre": "Iriome",
        "apellido": "Santana",
        "está_emocionado": True,
        "altura": 1.72,
        "dato_repetido": "Santana"
    }
print(diccionario["nombre"], diccionario["apellido"])
print(diccionario["altura"])