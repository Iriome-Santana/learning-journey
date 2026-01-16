
#Creando una lista usando la función list()
lista = list(["Hola", "Iriome", 54, True])


#Usando la función len() para obtener la cantidad de elementos en una lista
cantidad_elementos = len(lista)

#Agregando elementos a la lista con append()
lista.append("Paola")

#Agregando elementos a la lista con insert() en una posición específica
lista.insert(2, 777)

#Agregando varios elementos a la lista con extend()
lista.extend(["JAJAJA", False])

#eliminando un elemento de la lista por su indice
lista.pop(0)#-1 elimina el ultimo elemento, -2 el penultimo, etc

#eliminando un elemento de la lista por su valor
lista.remove("JAJAJA")

#eliminando todos los elementos de la lista
#lista.clear()

#ordenando una lista de forma ascendente solo funciona con numeros y True y False
lista_sort = [5, 2, 9, 1, 7]     
lista_sort.sort()  # La lista numeros ahora es [1, 2, 5, 7, 9]

#ordenando una lista de forma descendente
#lista_sort.sort(reverse=True)  # La lista numeros ahora es [9, 7, 5, 2, 1]

#invirtiendo el orden de los elementos en una lista (el ultimo pasa a ser el primero, el penultimo el segundo, etc)
#lista_sort.reverse() 

#verificando si un elemento existe en la lista
elemento_encontrado = lista.index(54)  # Devuelve el índice del elemento 54

print(elemento_encontrado) 