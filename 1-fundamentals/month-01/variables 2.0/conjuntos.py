#creando un conjunto con set

conjunto = set(["Dato1", "Dato2"])

#metiendo un conjunto en otro conjunto
conjunto1 = frozenset(["Dato1", "dato2"])
conjunto2 = {conjunto1, "Dato3"}
print(conjunto2)

#Teoria de conjuntos

conjunto1 = {1,3,5,7}
conjunto2 = {1,3,7}

#verificando si es un subconjunto
resultado = conjunto2.issubset(conjunto1)

#verificando si es un superconjunto
resultado1 = conjunto2.issuperset(conjunto1)

#verificando si hay un dato igual siempre que haya aunque sea un dato igual es False
resultado = conjunto2.isdisjoint(conjunto1)

print(resultado)