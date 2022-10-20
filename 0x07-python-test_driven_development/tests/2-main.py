#!/usr/bin/python3
matrix_divided = __import__('2-matrix_divided').matrix_divided

matrix = [
        [1, 2, 3],
        [4, 5, 6]
    ]

"""Testing basic divisions"""
print()
print("Testing basic divisions")
print("=======================")
print(matrix_divided(matrix, 3))
print(matrix)
print(matrix_divided(matrix, 155))
print(matrix_divided(matrix, 1000000))
print(matrix_divided([[3]], 5))
print(matrix_divided([[3],[6]], 5))
print()
print("Negative argument")
print("------------------")
print(matrix_divided([[-14],[-13]], -5))
print(matrix_divided(matrix , 10 - 5))
print(matrix_divided(matrix , -100000))
print()
print("Mixed integers and floats")
print("-------------------------")
print(matrix_divided(matrix, -3.5))
print(matrix_divided([[3.4, 6],[18, 4.46]], 1.3))

"""Infinity"""
print()
print("Infinity")
print("---------")
print(matrix_divided(matrix, float('inf')))
print(matrix_divided(matrix, float('NaN')))

"""Handle Erros , typerrorss"""
print()
print("Handle Erros , typerrors")
print("-------------------------")
matrix = [[2, 3, 4], [4, 5, 6], [4, 5, 6]]

try:
    print(matrix_divided(matrix, 0))
except Exception as e:
    print(e)

try:
    print(matrix_divided(matrix, "hello"))
except Exception as e:
    print(e)

matrix = [[2, 3, 4], [4, 5, 6, 3], [5, 6]]

try:
    print(matrix_divided(matrix, 13))
except Exception as e:
    print(e)

matrix = [[2, 3, "hola"], [4, "bob", 6, 3], [5, 6]]

try:
    print(matrix_divided(matrix, 13))
except Exception as e:
    print(e)

matrix = [[2, 3, 3], {3, 4}, [5, 6]]

try:
    print(matrix_divided(matrix, 13))
except Exception as e:
    print(e)

try:
    print(matrix_divided(None, 13))
except Exception as e:
    print(e)

matrix = []

try:
    print(matrix_divided(matrix, 13))
except Exception as e:
    print(e)

matrix = [[], [], []]
try:
    print(matrix_divided(matrix, 15))
except Exception as e:
    print(e)

matrix = [[1, 3, 4], (1, 2, 3), [1, 2, 3]]

try:
    print(matrix_divided(matrix, 16))
except Exception as e:
    print(e)

try:
    print(matrix_divided(matrix, 16, 3))
except Exception as e:
    print(e)

try:
    print(matrix_divided(matrix))
except Exception as e:
    print(e)

try:
    print(matrix_divided())
except Exception as e:
    print(e)

print()
