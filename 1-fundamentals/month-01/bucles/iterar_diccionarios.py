diccionario = {
    "nombre": "Iriome",
    "apellido": "Santana",
    "edad": 18
}

"""recorriendo el diccionario para obtener la clave(key)"""
for key in diccionario:
    print(f"La clave de este diccionario es: {key}")



"""recorriendo el diccionario con items() para obtener la clave(key) y el valor(value)"""
for dato in diccionario.items():
    key = dato[0]
    value = dato[1]
    print(f"La key de este diccionario es: {key} y el valor es: {value}")
    


    
    