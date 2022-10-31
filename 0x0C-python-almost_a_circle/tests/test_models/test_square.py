#!/usr/bin/python3
"""
test cases for square class
"""

import unittest
import io
import os
import json
import pep8
from models import square
from models.base import Base
from contextlib import redirect_stdout
Square = square.Square


class Test_Rectangle_creation(unittest.TestCase):
    """A class to test Rectangle Class"""
    def test_pep8_base(self):
        """
        Test that checks PEP8
        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/square.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )


class testcases(unittest.TestCase):
    """testing square class"""
    @classmethod
    def setUpClass(cls):
        """test"""
        Base._Base_objects = 0
        cls.c1 = Square(1)
        cls.c2 = Square(2, 3)
        cls.c3 = Square(3, 4, 5)
        cls.c4 = Square(5, 6, 7)
        cls.c5 = Square(7, 8, 9, 10)
        cls.c1.id = 1
        cls.c2.id = 2
        cls.c3.id = 3
        cls.c4.id = 4
        cls.c5.id = 10

    def test_id(self):
        """test"""
        self.assertEqual(self.c1.id, 1)
        self.assertEqual(self.c2.id, 2)
        self.assertEqual(self.c3.id, 3)
        self.assertEqual(self.c4.id, 4)
        self.assertEqual(self.c5.id, 10)

    def test_size(self):
        """test"""
        self.assertEqual(self.c1.size, 1)
        self.assertEqual(self.c2.size, 2)
        self.assertEqual(self.c3.size, 3)
        self.assertEqual(self.c4.size, 5)
        self.assertEqual(self.c5.size, 7)

    def test_width(self):
        """test"""
        self.assertEqual(self.c1.width, 1)
        self.assertEqual(self.c2.width, 2)
        self.assertEqual(self.c3.width, 3)
        self.assertEqual(self.c4.width, 5)
        self.assertEqual(self.c5.width, 7)

    def test_height(self):
        """test"""
        self.assertEqual(self.c1.height, 1)
        self.assertEqual(self.c2.height, 2)
        self.assertEqual(self.c3.height, 3)
        self.assertEqual(self.c4.height, 5)
        self.assertEqual(self.c5.height, 7)

    def test_x(self):
        """test"""
        self.assertEqual(self.c1.x, 0)
        self.assertEqual(self.c2.x, 3)
        self.assertEqual(self.c3.x, 4)
        self.assertEqual(self.c4.x, 6)
        self.assertEqual(self.c5.x, 8)

    def test_y(self):
        """test"""
        self.assertEqual(self.c1.y, 0)
        self.assertEqual(self.c2.y, 0)
        self.assertEqual(self.c3.y, 5)
        self.assertEqual(self.c4.y, 7)
        self.assertEqual(self.c5.y, 9)

    def test_arg(self):
        """test"""
        with self.assertRaises(TypeError):
            s = Square()

    def testing_size_typerror(self):
        """testing typerror error for size"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square("fizz")
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square(False)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            s = Square([1, 3])

    def testing_x_typerror(self):
        """testing typerror error for x"""
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, "fizz")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(1, False)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            s = Square(3, [1, 3])

    def testing_y_typerror(self):
        """testing typerror error for y"""
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 3, "fizz")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(1, 2,  False)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            s = Square(3, 4, [1, 3])

    def testing_size_valuerror(self):
        """testing value error for size"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            s = Square(0)

    def testing_x_valuerror(self):
        """testing value error for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            s = Square(1, -1)

    def testing_y_valuerror(self):
        """testing value error for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            s = Square(1, 1, -1)

    def test_area(self):
        """Testing area, assigments comes from lines 19"""
        self.assertEqual(self.c1.area(), 1)
        self.assertEqual(self.c2.area(), 4)
        self.assertEqual(self.c3.area(), 9)
        self.assertEqual(self.c4.area(), 25)
        self.assertEqual(self.c5.area(), 49)

    def test_area_args(self):
        """we just can call area, not pass args"""
        with self.assertRaises(TypeError):
            self.c1.area(1)

    def test_display(self):
        """tesing display aoutput"""
        test = Square(3, 0, 0, 3)
        with io.StringIO() as fi, redirect_stdout(fi):
            self.c1.display()
            output = fi.getvalue()
            self.assertEqual(output, "#\n")

        with io.StringIO() as fi, redirect_stdout(fi):
            test.display()
            output = fi.getvalue()
            self.assertEqual(output, ("#" * 3 + "\n") * 3)

    def test_display_arg(self):
        """we just can call display, no pars args"""
        with self.assertRaises(TypeError):
            self.c1.display(1)

    def test_str(self):
        """testing __str__"""
        self.assertEqual(str(self.c1), "[Square] (1) 0/0 - 1")
        self.assertEqual(str(self.c2), "[Square] (2) 3/0 - 2")
        self.assertEqual(str(self.c3), "[Square] (3) 4/5 - 3")
        self.assertEqual(str(self.c4), "[Square] (4) 6/7 - 5")
        self.assertEqual(str(self.c5), "[Square] (10) 8/9 - 7")

    def test_display_x_y(self):
        """tesing display x-y"""
        test = Square(3, 4)
        with io.StringIO() as fi, redirect_stdout(fi):
            test.display()
            output = fi.getvalue()
            self.assertEqual(output, (" " * 4 + "#" * 3 + "\n") * 3)

        test = Square(3, 4, 6)
        with io.StringIO() as fi, redirect_stdout(fi):
            test.display()
            output = fi.getvalue()
            self.assertEqual(output, "\n" * 6 + (" " * 4 + "#" * 3 + "\n") * 3)

        test = Square(3, 4, 4, 10)
        with io.StringIO() as fi, redirect_stdout(fi):
            test.display()
            output = fi.getvalue()
            self.assertEqual(output, "\n" * 4 + (" " * 4 + "#" * 3 + "\n") * 3)

    def test_uptadint_args(self):
        """testing update *args"""
        test = Square(13, 0, 0, 14)
        self.assertEqual(str(test), "[Square] (14) 0/0 - 13")

        test = Square(13, 3, 0, 14)
        self.assertEqual(str(test), "[Square] (14) 3/0 - 13")

        test = Square(13, 20, 23, 14)
        self.assertEqual(str(test), "[Square] (14) 20/23 - 13")

    def test_update_errors(self):
        """ testing setter with update"""
        test = Square(1, 3, 6, 7)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            test.update(1, "helloworld")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            test.update(1, 2, "helloworld")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            test.update(1, 2, 3, "helloworld")

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            test.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            test.update(1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            test.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            test.update(1, 1, 1, -1)

    def test_update_error_arg(self):
        """parsing more than 4 args to update"""
        test = Square(1, 2, 5, 1)
        test.update(1, 2, 3, 4, 5)
        self.assertEqual(str(test), "[Square] (1) 3/4 - 2")

    def test_update_no_args(self):
        """empty args"""
        test = Square(1, 2, 3, 4)
        test.update()
        self.assertEqual(str(test), "[Square] (4) 2/3 - 1")

    def test_update_kwargs(self):
        """testing kwargs updating"""
        test = Square(1, 0, 0, 1)
        self.assertEqual(str(test), "[Square] (1) 0/0 - 1")
        test.update(size=13)
        self.assertEqual(str(test), "[Square] (1) 0/0 - 13")
        test.update(size=13, x=3)
        self.assertEqual(str(test), "[Square] (1) 3/0 - 13")
        test.update(y=3, size=23, x=5, id=43)
        self.assertEqual(str(test), "[Square] (43) 5/3 - 23")

    def test_update_kwargs_setter(self):
        """testing setters with kwargs"""
        s = Square(1, 1, 1, 1)
        with self.assertRaises(TypeError):
            s.update(size=[3, 4])
        with self.assertRaises(TypeError):
            s.update(x="tasty")
        with self.assertRaises(TypeError):
            s.update(y="hello")
        with self.assertRaises(ValueError):
            s.update(size=-1)
        with self.assertRaises(ValueError):
            s.update(size=0)
        with self.assertRaises(ValueError):
            s.update(x=-1)
        with self.assertRaises(ValueError):
            s.update(y=-1)

    def test_to_dict(self):
        """testting dictionary"""
        test1 = self.c1.to_dictionary()
        self.assertEqual({"id": 1, "size": 1, "x": 0, "y": 0}, test1)
        test2 = self.c2.to_dictionary()
        self.assertEqual({"id": 2, "size": 2, "x": 3, "y": 0}, test2)
        test3 = self.c3.to_dictionary()
        self.assertEqual({"id": 3, "size": 3, "x": 4, "y": 5}, test3)
        test4 = self.c4.to_dictionary()
        self.assertEqual({"id": 4, "size": 5, "x": 6, "y": 7}, test4)
        self.assertTrue(type(test1) is dict)
        self.assertTrue(type(test2) is dict)
        self.assertTrue(type(test3) is dict)
        self.assertTrue(type(test4) is dict)
        test5 = Square(1, 1, 1, 1)
        test5.update(**test4)
        self.assertEqual(str(test5), str(self.c4))
        self.assertNotEqual(test5, self.c4)

    def test_save_to_file(self):
        """testing save_to_file"""
        test1 = Square(1, 1, 1, 1)
        test2 = Square(2, 2, 2, 2)
        tel = [test1, test2]
        Square.save_to_file(tel)
        with open("Square.json", "r") as file:
            ls = [test1.to_dictionary(), test2.to_dictionary()]
            self.assertEqual(json.dumps(ls), file.read())

    def test_empty_str(self):
        """pasing empy string"""
        tel = []
        Square.save_to_file(tel)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_none_str(self):
        """parsing none"""
        Square.save_to_file(None)
        with open("Square.json", "r") as file:
            self.assertEqual("[]", file.read())

    def test_create(self):
        """testing create"""
        test1 = {"id": 2, "size": 3, "x": 4, "y": 0}
        test2 = {"id": 9, "size": 6, "x": 7, "y": 8}
        test1c = Square.create(**test1)
        test2c = Square.create(**test2)
        self.assertEqual("[Square] (2) 4/0 - 3", str(test1c))
        self.assertEqual("[Square] (9) 7/8 - 6", str(test2c))
        self.assertIsNot(test1, test1c)
        self.assertIsNot(test2, test2c)
        self.assertNotEqual(test1, test1c)
        self.assertNotEqual(test2, test2c)

    def test_loadfromfile(self):
        """testing load_from_file"""
        try:
            os.remove("Square.json")
        except Exception as e:
            pass
        self.assertEqual(Square.load_from_file(), [])

    def test_empty_load(self):
        """loading empy file"""
        try:
            os.remove("Square.json")
        except Exception as e:
            pass
        open("Square.json", 'a').close()

    def test_load_f_file(self):
        """testing normal cases load file"""
        test1 = Square(2, 3, 4, 5)
        test2 = Square(7, 8, 9, 10)
        li = [test1, test2]
        Square.save_to_file(li)
        lo = Square.load_from_file()
        self.assertTrue(type(lo) is list)
        self.assertEqual(len(lo), 2)
        test1c = lo[0]
        test2c = lo[1]
        self.assertTrue(type(test1c) is Square)
        self.assertTrue(type(test2c) is Square)
        self.assertEqual(str(test1), str(test1c))
        self.assertEqual(str(test2), str(test2c))
        self.assertIsNot(test1, test1c)
        self.assertIsNot(test2, test2c)
        self.assertNotEqual(test1, test1c)
        self.assertNotEqual(test2, test2c)
