#!/usr/bin/python3
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

'''Show test file'''

class TestShowCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_show_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_show_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show MyClass"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_show_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show BaseModel"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_show_valid_input(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show BaseModel 123"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")


if __name__ == '__main__':
    unittest.main()
