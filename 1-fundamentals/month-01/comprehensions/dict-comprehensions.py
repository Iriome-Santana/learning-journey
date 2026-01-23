

"""Basic dict comprehensions"""
squares = {x: x**2 for x in range(10)}
print(squares)

"""Dict comprehensions with condition"""
squares = {x: x**2 for x in range(10) if x % 2 == 0}
print(squares)

"""Counting characters in a word"""
word = "hello"
word_count = {char: word.count(char) for char in word}
print(word_count)

"""Adding tax to prices"""
prices = {"apple": 0.5, "orange": 0.3, "banana": 0.8}
price_with_tax = {fruit: price * 1.21 for fruit, price in prices.items()}
print(price_with_tax)

"""Filtering expensive items"""
expensive = {fruit: price for fruit, price in prices.items() if price > 0.5}
print(expensive)

"""Filtering users"""
users = {"ana": 17, "luis": 21, "maria": 30}

mayors = {name: age for name, age in users.items() if age >= 18}
print(mayors)

