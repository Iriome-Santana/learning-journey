diccionario = {
    "nombre": "Iriome",
    "edad": 18,
    "guapa":"Paola"
}

claves = diccionario.keys()  # Obtiene todas las claves del diccionario
get = diccionario.get("nombre")  # Obtiene el valor asociado y si no existe devuelve None
#diccionario.clear() #elimina todo el diccionario
diccionario.pop("edad")  # Elimina el elemento con la clave especificada
diccionario_iterable = diccionario.items()  # Obtiene una vista de tuplas (clave, valor) del diccionario
diccionario["edad"] = 19  # Agrega o actualiza el valor asociado a la clave "edad"
print(diccionario_iterable)