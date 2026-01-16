numeros = [1, 7, 14, 51, 23]

"""encontrando el numero mayor de un iterable con max() (usamos min() para el mas bajo)"""

numero_mas_alto = max(numeros)
print(numero_mas_alto)

"""redondeando un numero"""
numero = round(12.4374422,2)
print(numero)

"""retorna False si es 0, vacio, None o False y True si es distinto de 0, True, cadena o datos no vacíos"""

resultado_bool = bool()

"""retorna True si todos los resultados son verdaderos"""
resultado_all = all([12, "cnbsjk", [45, True]])

"""suma todos los resultados de un iterable siempre que sean numeros"""
suma = sum(numeros)
print(suma)