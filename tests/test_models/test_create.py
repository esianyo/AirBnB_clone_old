#!/usr/bin/python
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

''' Testing create'''

class TestCreateCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_create_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_create_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create MyClass"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_create_valid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("create BaseModel"))
            output = f.getvalue().strip()
            self.assertIsInstance(output, str)
            self.assertNotEqual(output, "")


if __name__ == '__main__':
    unittest.main()
