#!/usr/bin/python3
import unittest
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO

'''Count test file'''

class TestCountCommand(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()

    def tearDown(self):
        pass

    def test_count_valid_class(self):
        with patch('sys.stdout', new=StringIO()) as f:
            self.assertTrue(self.console.onecmd("count BaseModel"))
            output = f.getvalue().strip()
            self.assertIsInstance(output, str)
            self.assertNotEqual(output, "")


if __name__ == '__main__':
    unittest.main()
