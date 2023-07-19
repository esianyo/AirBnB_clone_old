#!/usr/bin/python3
"""Console unittests"""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):

    def test_create(self):
        """Test the create command"""
        cmd = HBNBCommand()
        result = cmd.onecmd("create User")
        self.assertEqual(result, "1")

    def test_show(self):
        """Test the show command"""
        cmd = HBNBCommand()
        cmd.onecmd("create User")
        result = cmd.onecmd("show User 1")
        self.assertEqual(result, "{}".format(cmd.all['User.1']))

    def test_destroy(self):
        """Test the destroy command"""
        cmd = HBNBCommand()
        cmd.onecmd("create User")
        result = cmd.onecmd("destroy User 1")
        self.assertEqual(result, "")

    def test_all(self):
        """Test the all command"""
        cmd = HBNBCommand()
        cmd.onecmd("create User")
        cmd.onecmd("create Amenity")
        result = cmd.onecmd("all")
        self.assertIn("User.1", result)
        self.assertIn("Amenity.1", result)

    def test_update(self):
        """Test the update command"""
        cmd = HBNBCommand()
        cmd.onecmd("create User")
        result = cmd.onecmd("update User 1 name John")
        self.assertEqual(result, "{}".format(cmd.all['User.1']))

    def test_default(self):
        """Test the default command"""
        cmd = HBNBCommand()
        result = cmd.onecmd("help show")
        self.assertIn("show", result)


if __name__ == "__main__":
    unittest.main()
