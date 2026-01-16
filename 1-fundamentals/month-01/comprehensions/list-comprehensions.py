"""Basic List Comprehension"""
lst = [i for i in range(11)]
print(lst)

"""List Comprehension with Condition"""
even_lst = [i for i in range(11) if i % 2 == 0]
print(even_lst)

"""List Comprehension with Function"""
def square(n):
    n = int(input("Enter a number to square: "))
    return n * n
squared_lst = [square(i) for i in range(11)]
print(squared_lst)

"""Nested List Comprehension"""
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [num for row in matrix for num in row]
print(flattened)