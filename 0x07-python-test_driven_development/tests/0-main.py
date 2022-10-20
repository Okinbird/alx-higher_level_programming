#!/usr/bin/python3
add_integer = __import__('0-add_integer').add_integer
print("Testing general additions:")
print("---------")
print(add_integer(1, 2))
print(add_integer(100, -2))
print(add_integer(2))
print(add_integer(100.3, -2))
print("")

"""Testing b(98) as default number:"""

print("Testing b(98) as default number:")
print("---------")
print(add_integer(10))
print(add_integer(-5))
print()


"""Testing message errors:"""
print("Testing message errors:")
print("---------")
try:
    print(add_integer(4, "School"))
except Exception as e:
    print(e)
try:
    print(add_integer(None))
except Exception as e:
    print(e)
print()

"""Check for documentation """
print("tesint documentation:")
print("---------")
module_doc = __import__("0-add_integer").__doc__
print(len(module_doc) > 0)
funciont_doc = __import__("0-add_integer").add_integer.__doc__
print(len(funciont_doc) > 0)
print()

"""testing big numbers"""
print("testing big numbers")
print("---------")
print(add_integer(2147483648214748364821474836482147483648, 2))
print()
print("testing negative numbers")
print("---------")
print(add_integer(-5, -5))
print(add_integer(15, -5))
print(add_integer(-15, 5))
print()

"""testing float numbers"""
print("Testing float numbers")
print("---------")
print(add_integer(13.5, 5))
print(add_integer(13.8, 5.3))
print(add_integer(-13.8, -5.34))
print()

"""Testint infinity and None"""
print("Testing infinity and None")
print("---------")
try:
    print(add_integer(None))
except Exception as e:
    print(e)

try:
    print(add_integer(float('inf')))
except Exception as e:
    print(e)

try:
    print(add_integer(float('NaN')))
except Exception as e:
    print(e)
print()

"""Typer Errros"""
print("Type Errors")
print("---------")
try:
    print(add_integer(2, "hola"))
except Exception as e:
    print(e)

try:
    print(add_integer("hola", 3))
except Exception as e:
    print(e)

try:
    print(add_integer({'hola', 3}, 2))
except Exception as e:
    print(e)

try:
    print(add_integer(15, [2, 3]))
except Exception as e:
    print(e)
print()

"""Bool False True"""
print("Bool False True")
print("---------")
try:
    print(add_integer(15, False))
except Exception as e:
    print(e)

try:
    print(add_integer(True, 33))
except Exception as e:
    print(e)
print()

""""Testing arguments"""
print("Testing arguments")
print("---------")

try:
    print(add_integer())
except Exception as e:
    print(e)

print(add_integer(23))

try:
    print(add_integer(3, 4, 13))
except Exception as e:
    print(e)

print()
