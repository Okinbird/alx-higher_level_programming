#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.square(5)
print("Area: {} - Perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
print()
mysquare = Rectangle.square(10)
print("Width: {} / height: {}".format(mysquare.width, my_square.height))
print()
mysquare = Rectangle.square(2)
print("{} / {}".format(mysquare.width, my_square.height))
print()

mysquare = Rectangle.square(-2)
print("{} / {}".format(mysquare.width, mysquare.height))
except Exception as e:
    print("[{}] {}".format(e.class.name_, e))
print()

mysquare = Rectangle.square("12")
print("{} / {}".format(mysquare.width, mysquare.height))
except Exception as e:
    print("[{}] {}".format(e.class.name_, e))
