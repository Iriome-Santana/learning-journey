#creando diccionarios con dict sirve para hacer diccionarios vacíos

diccionario = dict(nombre="Iriome", apellido="Santana")

#las listas no pueden ser CLAVES pero las tuplas si y usamos frozenset para conjuntos
diccionario = {("si","despues"): "Mañana"}

#creando diccionarios con fromkeys() valor por defecto None
diccionario = dict.fromkeys(["nombre", "apellidos"])

#creando diccionarios con fromkeys() cambiando el valor por defecto no se
diccionario = dict.fromkeys(["nombre", "apellidos"], "no se")


print(diccionario)