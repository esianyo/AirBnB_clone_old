#!/usr/bin/python3
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

'''All test file'''

class TestAllCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_all_missing_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("all"))
            output = f.getvalue().strip()
            self.assertIsInstance(output, str)
            self.assertNotEqual(output, "")

    def test_all_invalid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all MyClass"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_all_valid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("all BaseModel"))
            output = f.getvalue().strip()
            self.assertIsInstance(output, str)
            self.assertNotEqual(output, "")


if __name__ == '__main__':
    unittest.main()
