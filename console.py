#!/usr/bin/python3
"""Console Module"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Contains the functionality for the HBNB console"""

    prompt = '(hbnb) ' if sys.__stdin__.isatty() else ''
    classes = {
        'BaseModel': BaseModel, 'User': User, 'Place': Place,
        'State': State, 'City': City, 'Amenity': Amenity,
        'Review': Review
    }
    dot_cmds = ['all', 'count', 'show', 'destroy', 'update']
    types = {
        'number_rooms': int, 'number_bathrooms': int,
        'max_guest': int, 'price_by_night': int,
        'latitude': float, 'longitude': float
    }

    def preloop(self):
        if not sys.__stdin__.isatty():
            print('(hbnb)')

    def precmd(self, line):
        if not ('.' in line and '(' in line and ')' in line):
            return line

        try:
            parts = line.split('.')
            cls = parts[0]
            cmd_and_args = parts[1].split('(')
            cmd = cmd_and_args[0]
            args = cmd_and_args[1].strip(')')

            if '{' in args and '}' in args:
                args_dict = eval(args)
                args = ' '.join([f'{k}={v}' for k, v in args_dict.items()])

            line = f'{cmd} {cls} {args}'
        except Exception as e:
            pass
        finally:
            return line

    def postcmd(self, stop, line):
        if not sys.__stdin__.isatty():
            print('(hbnb) ', end='')
        return stop

    def do_quit(self, command):
        exit()

    def help_quit(self):
        print("Exits the program with formatting\n")

    def do_EOF(self, arg):
        print()
        exit()

    def help_EOF(self):
        print("Exits the program without formatting\n")

    def emptyline(self):
        pass

    def do_create(self, args):
        try:
            if not args:
                raise SyntaxError()
            arg_list = args.split(" ")
            kwargs = {arg.split("=")[0]: eval(arg.split("=")[1]) for arg in arg_list[1:]}
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        else:
            new_instance = HBNBCommand.classes[arg_list[0]](**kwargs)
            new_instance.save()
            print(new_instance.id)

    def help_create(self):
        print("Creates a class of any type")
        print("[Usage]: create <className>\n")

    def do_show(self, args):
        new = args.partition(" ")
        cls_name = new[0]
        obj_id = new[2].split(' ')[0] if new[2] and ' ' in new[2] else None

        if not cls_name:
            print("** class name missing **")
            return

        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not obj_id:
            print("** instance id missing **")
            return

        key = f"{cls_name}.{obj_id}"
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def help_show(self):
        print("Shows an individual instance of a class")
        print("[Usage]: show <className> <objectId>\n")

    def do_destroy(self, args):
        new = args.partition(" ")
        cls_name = new[0]
        obj_id = new[2].split(' ')[0] if new[2] and ' ' in new[2] else None

        if not cls_name:
            print("** class name missing **")
            return

        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        if not obj_id:
            print("** instance id missing **")
            return

        key = f"{cls_name}.{obj_id}"

        try:
            del(storage.all()[key])
            storage.save()
        except KeyError:
            print("** no instance found **")

    def help_destroy(self):
        print("Destroys an individual instance of a class")
        print("[Usage]: destroy <className> <objectId>\n")

    def do_all(self, args):
        print_list = []

        if args:
            args = args.split(' ')[0]
            if args not in HBNBCommand.classes:
                print("** class doesn't exist **")
                return
            for k, v in storage.all(HBNBCommand.classes[args]).items():
                print_list.append(str(v))
        else:
            for k, v in storage.all().items():
                print_list.append(str(v))
        print(print_list)

    def help_all(self):
        print("Shows all objects, or all of a class")
        print("[Usage]: all <className>\n")

    def do_count(self, args):
        count = sum(1 for k in storage.all() if args == k.split('.')[0])
        print(count)

    def help_count(self):
        print("Usage: count <class_name>")

    def do_update(self, args):
        cls_name, obj_id, att_name, att_val, kwargs = '', '', '', '', ''

        parts = args.split(" ")
        if parts[0]:
            cls_name = parts[0]
        else:
            print("** class name missing **")
            return

        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return

        parts = parts[1].split(" ")
        if parts[0]:
            obj_id = parts[0]
        else:
            print("** instance id missing **")
            return

        key = f"{cls_name}.{obj_id}"

        if key not in storage.all():
            print("** no instance found **")
            return

        parts = parts[1]
        if '{' in parts and '}' in parts and type(eval(parts)) is dict:
            kwargs = eval(parts)
            args = [f'{k}={v}' for k, v in kwargs.items()]
        else:
            args = parts.split(' ')
            if args[0] == '\"':
                second_quote = args.find('\"', 1)
                att_name = args[1:second_quote]
                args = args[second_quote + 1:]

            args = args.partition(' ')
            if not att_name and args[0] != ' ':
                att_name = args[0]

            if args[2] and args[2][0] == '\"':
                att_val = args[2][1:args[2].find('\"', 1)]

            if not att_val and args[2]:
                att_val = args[2].partition(' ')[0]

            args = [att_name, att_val]

        new_dict = storage.all()[key]

        for i, att_name in enumerate(args):
            if (i % 2 == 0):
                att_val = args[i + 1]
                if not att_name:
                    print("** attribute name missing **")
                    return
                if not att_val:
                    print("** value missing **")
                    return

                if att_name in HBNBCommand.types:
                    att_val = HBNBCommand.types[att_name](att_val)

                new_dict.__dict__.update({att_name: att_val})

        new_dict.save()

    def help_update(self):
        print("Updates an object with new information")
        print("Usage: update <className> <id> <attName> <attVal>\n")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
