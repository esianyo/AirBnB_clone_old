#!/usr/bin/python3
"""Test for the console"""
import unittest
from unittest.mock import patch
from io import StringIO
import console
from console import HBNBCommand
from models import storage


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_quit(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("quit"))
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_EOF(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("EOF"))
            output = f.getvalue().strip()
            self.assertEqual(output, "")

    def test_create(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("create MyClass"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("create BaseModel"))
            output = f.getvalue().strip()
            self.assertIsInstance(output, str)
            self.assertNotEqual(output, "")

    def test_show(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show MyClass"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show BaseModel"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("show BaseModel 123"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_destroy(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy MyClass"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy BaseModel"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("destroy BaseModel 123"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_all(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("all"))
            output = f.getvalue().strip()
            self.assertIsInstance(output, str)
            self.assertNotEqual(output, "")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("all MyClass"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

    def test_update(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class name missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update MyClass"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** class doesn't exist **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** instance id missing **")

        with patch('sys.stdout', new=StringIO()) as f:
            self.assertFalse(self.console.onecmd("update BaseModel 123"))
            output = f.getvalue().strip()
            self.assertEqual(output, "** no instance found **")

    def test_count(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("count BaseModel"))
            output = f.getvalue().strip()
            self.assertIsInstance(output, str)
            self.assertNotEqual(output, "")


if __name__ == '__main__':
    unittest.main()
