## 0x0C. Python - Almost a circle



#  0. If it's not tested it doesn't work

All your files, classes and methods must be unit tested and be PEP 8 validated.
```
guillaume@ubuntu:~/$ python3 -m unittest discover tests
...................................................................................
...................................................................................
.......................
----------------------------------------------------------------------
Ran 189 tests in 13.135s

OK
guillaume@ubuntu:~/$
```
*Note that this is just an example. The number of tests you create can be different from the above example.*



#  1. Base class

Write the first class `Base`:

Create a folder named `models` with an empty file `__init__.py` inside - with this file, the folder will become a Python package

Create a file named `models/base.py`:

*   Class `Base`:
        -  private class attribute `__nb_objects = 0`
	-  class constructor: `def __init__(self, id=None):`:
               +  if `id` is not `None`, assign the public instance attribute `id` with this argument value - you can assume `id` is an integer and you don’t need to test the type of it
	       +  otherwise, increment `__nb_objects` and assign the new value to the public instance attribute `id`

This class will be the “base” of all other classes in this project. The goal of it is to manage `id` attribute in all your future classes and to avoid duplicating the same code (by extension, same bugs)


