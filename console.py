#!/usr/bin/python3
"""
Defines the HBnB console.

HBNBCommand class

Attributes:
    __classes (dict): A dictionary of all the classes that can be created.

Methods:
    emptyline (self): Does nothing.
    do_quit (self, line): Exits the shell.
    do_EOF (self, line): Exits the shell.
    do_create (self, args): Creates a new instance of a class.
    do_show (self, line): Prints the information of an instance.
    do_destroy (self, line): Deletes an instance.
    do_all (self, args): Prints all the instances of a class.
    do_update (self, args): Updates an instance.
    do_count (self, line): Counts the number of instances of a class.
    default (self, arg): Handles unknown commands.
"""


import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
import json

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """
    HBnB command interpreter.

    Attributes:
        prompt (str): The command prompt.
    """

    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    def emptyline(self):
        """Do nothing upon receiving an empty line."""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        argdict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
                }
        match = re.search(r"\.", arg)
        if match is not None:
            argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", argl[1])
            if match is not None:
                command = [argl[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in argdict.keys():
                    call = "{} {}".format(argl[0], command[1])
                    return argdict[command[0]](call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF signal to exit the program."""
        print("")
        return True

    def do_create(self, arg):
        """
        Usage: create <class>
        Create a new class instance and print its id.
        """
        argl = parse(arg)
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argl[0])().id)
            storage.save()

    def do_show(self, arg):
        """
        Usage: show <class> <id> or <class>.show(<id>)
        Display the string representation of a class instance of a given id.
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argl[0], argl[1])])

    def do_destroy(self, arg):
        """
        Usage: destroy <class> <id> or <class>.destroy(<id>)
        Delete a class instance of a given id.
        """
        argl = parse(arg)
        objdict = storage.all()
        if len(argl) == 0:
            print("** class name missing **")
        elif argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argl) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """
        Usage: all or all <class> or <class>.all()
        Display string representations of all instances of a given class.
        If no class is specified, displays all instantiated objects.
        """
        argl = parse(arg)
        if len(argl) > 0 and argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for obj in storage.all().values():
                if len(argl) > 0 and argl[0] == obj.__class__.__name__:
                    objl.append(obj.__str__())
                elif len(argl) == 0:
                    objl.append(obj.__str__())
            print(objl)

    def do_count(self, arg):
        """
        Usage:
            count <class> or <class>.count()
            Retrieve the number of instances of a given class.
        """
        argl = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """
        Usage:
            update <class> <id> <attribute_name> <attribute_value> or
            <class>.update(<id>, <attribute_name>, <attribute_value>) or
            <class>.update(<id>, <dictionary>)
            Update a class instance of a given id by adding or updating
            a given attribute key/value pair or dictionary.
        """
        argl = parse(arg)
        objdict = storage.all()

        if len(argl) == 0:
            print("** class name missing **")
            return False
        if argl[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(argl) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(argl[0], argl[1]) not in objdict.keys():
            print("** no instance found **")
            return False
        if len(argl) == 2:
            print("** attribute name missing **")
            return False
        if len(argl) == 3:
            try:
                type(eval(argl[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(argl) == 4:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            if argl[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[argl[2]])
                obj.__dict__[argl[2]] = valtype(argl[3])
            else:
                obj.__dict__[argl[2]] = argl[3]
        elif type(eval(argl[2])) == dict:
            obj = objdict["{}.{}".format(argl[0], argl[1])]
            for k, v in eval(argl[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

if __name__ == "__main__":


    class HBNBCommand(cmd.Cmd):
        """Type class HBNBCommand CLI"""
    prompt = '(hbnb) '
    __classes = {
            'BaseModel',
            'Amenity',
            'Place',
            'User',
            'State',
            'Review',
            'City'
            }

    def emptyline(self):
        """Type method emptyline"""
        pass

    def do_quit(self, line):
        """Exits the shell"""
        return True

    def do_EOF(self, line):
        """Exit the shell"""
        print()
        return True

    def do_create(self, args):
        """Type method create"""
        if not args:
            print('** class name missing **')
        elif args not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
        else:
            cls_d = {'BaseModel': BaseModel, 'User': User, 'Amenity': Amenity,
                    'City': City, 'Place': Place,
                    'Review': Review, 'State': State}
            new_obj = cls_d[args]()
            new_obj.save()
            print('{}'.format(new_obj.id))
            storage.save()

    def do_show(self, line):
        """Type method show"""
        arg = line.split()
        obj_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(arg[0], arg[1])])

    def do_destroy(self, line):
        """Type method destroy"""
        arg = line.split()
        obj_dict = storage.all()
        if len(arg) == 0:
            print("** class name missing **")
        elif arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg[0], arg[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(arg[0], arg[1])]
            storage.save()

    def do_all(self, args):
        """Type method all"""
        yes = 0
        all_obj = [str(v) for v in storage.all().values()]
        if not args:
            yes = 1
            print('{}'.format(all_obj))
        elif args:
            arg_list = args.split()
        if args and arg_list[0] in HBNBCommand.__classes:
            yes = 1
            all_obj = storage.all()
            name = arg_list[0]
            all_obj = [str(v) for k, v in all_obj.items()
                    if name == v.__class__.__name__]
            print(all_obj)

        if yes != 1:
            print('** class doesn\'t exist **')

    def do_update(self, args):
        """Type method update"""
        args_ = args.split()
        if not args:
            print('** class name missing **')
            return
        else:
            up_dir = re.search(r"(?<=\{)([^\}]+)(?=\})", args)
            all_obj = storage.all()
            yes = 0

        if args_[0] not in HBNBCommand.__classes:
            print('** class doesn\'t exist **')
        elif len(args_) < 2:
            print('** instance id missing **')
        else:
            for k, v in all_obj.items():
                iddd = args_[1].replace('"', '').replace(',', '')
                name_nw = args_[0] + '.' + iddd
                if name_nw == k:
                    yes = 1
                    if up_dir:

                        s_d = up_dir.group()
                        dir_s = '{' + s_d[:] + '}'
                        dir_s1 = dir_s.replace('\'', '"')
                        dir_ob = json.loads(dir_s1)
                        for u_k, u_v in dir_ob.items():
                            if u_k and u_v:
                                setattr(v, u_k, u_v)
                                storage.all()[name_nw].save()
                        return

                    elif len(args_) == 2:
                        print("** attribute name missing **")
                    elif len(args_) == 3:
                        print("** value missing **")
                    else:
                        value1 = str(args_[3]).replace('"', '')
                        valuee = value1.replace(',', '')
                        namev = str(args_[2]).replace('"', '').replace(',', '')
                        setattr(v, namev, valuee)
                        storage.all()[name_nw].save()
            if yes != 1:
                print("** no instance found **")

    def do_count(self, line):
        """Type method count"""
        arg = line.split()
        counter = 0
        for obj in storage.all().values():
            if arg[0] == obj.__class__.__name__:
                counter += 1
        print(counter)

    def default(self, arg):
        """Type method default"""
        m_dict = {
                "all": self.do_all,
                "show": self.do_show,
                "destroy": self.do_destroy,
                "count": self.do_count,
                "update": self.do_update
                }
        m = re.search(r"\.", arg)
        if m is not None:
            marg = [arg[:m.span()[0]], arg[m.span()[1]:]]
            m = re.search(r"\((.*?)\)", marg[1])
            if m is not None:
                cmd = [marg[1][:m.span()[0]], m.group()[1:-1]]
                if cmd[0] in m_dict.keys():
                    if cmd[0] == 'update':
                        up_dir = re.search(r"(?<=\{)([^\}]+)(?=\})", cmd[1])
                        up = cmd[1].split()
                        idd = up[0].replace('"', '').replace(',', '')
                        if up_dir:
                            content = up_dir.group()
                            dir_s = '{' + content[:] + '}'
                            r_ar = "{} {} {}".format(marg[0], idd, dir_s)
                            return m_dict['update'](r_ar)
                    get = "{} {}".format(marg[0], cmd[1].replace('"', ''))
                    return m_dict[cmd[0]](get)
        print("*** Unknown syntax: {}".format(arg))
        return False


if __name__ == '__main__':
    HBNBCommand().cmdloop()
