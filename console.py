#!/usr/bin/python3
"""
This module defines the entry point of the command interpreter.
"""

from models import storage
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Command to exit/quit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line."""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id
        """
        if not arg:
            print("** class name missing **")
            return
        if arg != "BaseModel":
            print("** class doesn't exist **")
            return
        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exit **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        print(obj)

    def do_destroy(self, arg):
        """deletes an instance based on the class name and id
        (save the changes into d JSON file.)
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] != "BaseModel":
            print("** calss doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in storage.all():
            print("** no instance found **")
            return
        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string rep of all instances based or
        not on the class name.
        """
        if arg and arg != "BaseModel":
            print("** class doesn't exist **")
            return
        objt_list = [
                str(obj) for obj in storage.all().values()
                if not arg or obj.__class__.__name__ == arg
        ]
        print(objt_list)

    def do_update(self, arg):
        """Upadtes instance based on d class name and id
        by adding or updating attribute.
        """
        args = arg.split()
        if len(args) == 0:
            print("** class anme missing **")
            return
        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        obj = storage.all().get(key)
        if obj is None:
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3].strip('"')
        try:
            if '.' in attr_value:
                attr_value = float(attr_value)
            else:
                attr_value = int(attr_value)
        except ValueError:
            pass
        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
