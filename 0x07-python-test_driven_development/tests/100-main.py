#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[1, 2]], [[3, 4], [5, 6]]))

b = [[1, 2], 1]
a = [[2, 9, 0], [1, 3, 5], [2, 4, 7], [8, 1, 5]]

try:
    print(matrix_mul(a, b))
except Exception as e:
    print(e)
a = []
b = [[1, 2],[2, 3]]
try:
    print(matrix_mul(a, b))
except Exception as e:
    print(e)

a = [[1, 2],[2, 3], [1, 2],[2, 3],[1, 2],[2, 3]]
b = [[1, 2, 3],[1, 2, 3]]
print(matrix_mul(a, b))

a = True
b = [[1, 2, 3],[1, 2, 3]]

try:
    print(matrix_mul(a, b))
except Exception as e:
    print(e)

b = True
a = [[1, 2, 3],[1, 2, 3]]

try:
    print(matrix_mul(a, b))
except Exception as e:
    print(e)

b = None
a = [[1, 2, 3],[1, 2, 3]]

try:
    print(matrix_mul(a, b))
except Exception as e:
    print(e)

b = 23
a = [[1, 2, 3],[1, 2, 3]]
try:
    print(matrix_mul(a, b))
except Exception as e:
    print(e)

try:
    print(matrix_mul([[1, 1]], [[2, 2], [2, 3]], [[3, 2], [3, 2]]))
except Exception as e:
    print(e)

try:
    print(matrix_mul([[1, 1]]))
except Exception as e:
    print(e)

print(matrix_mul([[1, 2], [3, 4, 5]], [[1, 2], [3, 4]]))
