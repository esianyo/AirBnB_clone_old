#!/usr/bin/python3
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

'''Update test file'''

class TestUpdateCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_update_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

    def test_update_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update MyClass"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update_missing_id(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

    def test_update_valid_input(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel 123"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")


if __name__ == '__main__':
    unittest.main()
