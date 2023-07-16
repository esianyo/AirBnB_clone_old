#!/usr/bin/python3
"""
Unittest for user module
"""
import os
import unittest
from models.user import User
import models
from datetime import datetime
from models.engine.file_storage import FileStorage


class Test_User(unittest.TestCase):
    """ Test Cases for
    User Class """

    def setUp(self):
        """set up the
        test for testing users"""
        FileStorage._FileStorage__file_path = "file.json"

    def test_args_None(self):
        usr = User(None)
        self.assertNotIn(None, usr.__dict__.values())

    def test_kwargs_None(self):
        with self.assertRaises(TypeError):
            User(id=None, created_at=None, updated_at=None)

    def test_public(self):
        self.assertEqual(str, type(User().id))

    def test_noarg(self):
        self.assertEqual(User, type(User()))

    def test_new_instance(self):
        self.assertIn(User(), models.storage.all().values())

    def test_create_datetime(self):
        self.assertEqual(datetime, type(User().created_at))

    def test_update_time(self):
        self.assertEqual(datetime, type(User().updated_at))

    def test_email(self):
        self.assertEqual(str, type(User.email))

    def test_password(self):
        self.assertEqual(str, type(User.password))

    def test_name(self):
        self.assertEqual(str, type(User.first_name))
        self.assertEqual(str, type(User.last_name))

    def test_multipleuser(self):
        usr1 = User()
        usr2 = User()
        self.assertNotEqual(usr1.id, usr2.id)

    def test_multipleuser_created(self):
        usr1 = User()
        usr2 = User()
        self.assertLess(usr1.created_at, usr2.created_at)

    def test_kawargs(self):
        datet = datetime.today()
        datei = datet.isoformat()
        usr = User(id="931", created_at=datei, updated_at=datei)
        self.assertEqual(usr.id, "931")
        self.assertEqual(usr.created_at, datet)
        self.assertEqual(usr.updated_at, datet)

    def test_args(self):
        datet = datetime.today()
        datei = datet.isoformat()
        dater = repr(datet)
        usr = User()
        usr.id = "931"
        usr.created_at = usr.updated_at = datet
        usr_str = usr.__str__()
        self.assertIn("[User] (931)", usr_str)
        self.assertIn("'id': '931'", usr_str)
        self.assertIn("'created_at': " + dater, usr_str)
        self.assertIn("'updated_at': " + dater, usr_str)


class TestSave(unittest.TestCase):

    def setUp(self):
        """set up the
        test for testing users"""
        FileStorage._FileStorage__file_path = "file.json"

    @classmethod
    def SetUp(self):
        try:
            os.rename("file.json", "temp")
        except IOError:
            pass

    def tearDown(self):
        try:
            os.remove("file.json")
        except IOError:
            pass

    def test_savearg(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.save(None)

    def test_save(self):
        usr = User()
        updt = usr.updated_at
        usr.save()
        self.assertLess(updt, usr.updated_at)

    def test_multiple_save(self):
        usr = User()
        updt = usr.updated_at
        usr.save()
        updt2 = usr.updated_at
        self.assertLess(updt, usr.updated_at)
        usr.save()
        self.assertLess(updt2, usr.updated_at)

    def test_save_updated(self):
        usr = User()
        usr.save()
        usrid = "User." + usr.id
        with open("file.json", "r") as f:
            self.assertIn(usrid, f.read())


class Testuser_dict(unittest.TestCase):

    def test_None(self):
        usr = User()
        with self.assertRaises(TypeError):
            usr.to_dict(None)

    def test_muldict(self):
        usr = User()
        self.assertNotEqual(usr.to_dict(), usr.__dict__)

    def test_dict_type(self):
        self.assertTrue(dict, type(User().to_dict()))

    def test_dict(self):
        usr = User()
        self.assertIn("id", usr.to_dict())
        self.assertIn("created_at", usr.to_dict())
        self.assertIn("updated_at", usr.to_dict())
        self.assertIn("__class__", usr.to_dict())

    def test_dict_str(self):
        usr = User()
        Dusr = usr.to_dict()
        self.assertEqual(str, type(Dusr['id']))
        self.assertEqual(str, type(Dusr["created_at"]))
        self.assertEqual(str, type(Dusr["updated_at"]))

    def test_dict_end(self):
        datet = datetime.today()
        datei = datet.isoformat()
        usr = User()
        usr.id = "931"
        usr.created_at = usr.updated_at = datet
        Dict = {
            "id": "931",
            "__class__":  "User",
            "created_at": datei,
            "updated_at": datei,
        }

    def test_dict_arg(self):
        usr = User()
        usr.name = "Betty"
        usr.number = 89
        self.assertEqual("Betty", usr.name)
        self.assertIn("number", usr.to_dict())


if __name__ == "__main__":
    unittest.main()
