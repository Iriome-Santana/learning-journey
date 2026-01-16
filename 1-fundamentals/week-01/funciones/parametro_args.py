#forma no optima de sumar valores
#def suma(lista):
 #   numeros_sumados = 0
  #  for numero in lista:
   #     numeros_sumados = numeros_sumados + numero
    #return numeros_sumados

#resultado = suma([5, 3, 8])


#utilizando el operador * como argumento (*args)

def suma(nombre, *numeros):
   return f"tu nombre es {nombre} y la suma de tus numeros es {sum(numeros)}"
    
resultado = suma("Iriome", 1, 4, 10, 5)
print(resultado)

#otra forma

def suma_total(numeros):
    return sum([*numeros])

resultado2 = suma_total([1, 4, 10, 5])
print(resultado2)