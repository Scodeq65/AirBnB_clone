#!/usr/bin/python3
"""
This module defines the entry point of the command interpreter.
"""

from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.city import City
from models import storage
from models.base_model import BaseModel
import cmd
from models.user import User
import shlex
import json


class HBNBCommand(cmd.Cmd):
    """Command interpreter class."""

    prompt = '(hbnb) '

    classes = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review
    }

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
        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[args[0]]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exit **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name, instance_id = args
        key = "{}.{}".format(class_name, instance_id)
        if key not in storage.all():
            print("** no instance found **")
        else:
            print(storage.all()[key])

    def do_destroy(self, arg):
        """deletes an instance based on the class name and id
        (save the changes into d JSON file.)
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
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
        args = shlex.split(arg)
        objects = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in objects.values()])
        elif args[0] in self.classes:
            print(
                    [str(obj) for obj in objects.values()
                        if type(obj).__name__ == args[0]]
            )
        else:
            print("** class doesn't exist **")

    def do_update(self, arg):
        """Upadtes instance based on d class name and id
        by adding or updating attribute.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key not in storage.all():
            print("** no instance found **")
            return
        obj = storage.all()[key]

        if len(args) == 3:
            try:
                data = json.loads(args[2].replace("'", '"'))
                if isinstance(data, dict):
                    for attr, value in data.items():
                        setattr(obj, attr, value)
                    obj.save()
                    return
            except json.JSONDecodeError:
                pass
            print("** invalid Dict rep **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(obj, args[2], args[3])
        obj.save()

    def do_count(self, class_name):
        """Get the number of instances of a class."""
        if class_name in self.classes:
            count = sum(
                    1 for obj in storage.all().values()
                    if type(obj).__name__ == class_name
            )
            print(count)
        else:
            print("** class doesn't exist **")

    def onecmd(self, line):
        """Override onecmd to handle <class name>.all() syntax."""
        args = line.split('.')
        if len(args) == 2:
            class_name = args[0]
            method_and_arg = args[1]
            if method_and_arg == "all()":
                if class_name in self.classes:
                    self.do_all(class_name)
                else:
                    print("** class doesn't exist **")
                return
            elif method_and_arg == "count()":
                self.do_count(class_name)
                return
            elif (method_and_arg.startswith("show(") and
                    method_and_arg.endswith(")")):
                instance_id = method_and_arg[5:-1]
                if class_name in self.classes:
                    self.do_show(f"{class_name} {instance_id}")
                else:
                    print("** class doesn't exist **")
                return
            elif (method_and_arg.startswith("destroy(") and
                    method_and_arg.endswith(")")):
                instance_id = method_and_arg[8:-1]
                if class_name in self.classes:
                    self.do_destroy(f"{class_name} {instance_id}")
                else:
                    print("** class doesn't exist **")
                return
            elif (method_and_arg.startswith("update(") and
                    method_and_arg.endswith(")")):
                update_args = method_and_arg[7:-1].split(',', 1)
                if len(update_args) == 2:
                    instance_id = update_args[0].strip()
                    try:
                        data = json.loads(
                                update_args[1].strip().replace("'", '"')
                        )
                        if isinstance(data, dict):
                            if class_name in self.classes:
                                self.do_update(
                                        f"{class_name} {instance_id} "
                                        f"{json.dumps(data)}"
                                )
                            else:
                                print("** class doesn't exist **")
                            return
                    except json.JSONDecodeError:
                        print("** invalid dictionary representation **")
                        return
                else:
                    update_args = method_and_arg[7:-1].split(',', 2)
                    if len(update_args) == 3:
                        instance_id, attr_name, attr_value = map(
                                str.strip, update_args
                        )
                        if class_name in self.classes:
                            self.do_update(
                                    f"{class_name} {instance_id} {attr_name} "
                                    f"{attr_value}"
                            )
                        else:
                            print("** class doesn't exist **")
                        return
                print("** invalid arguments **")
                return
        return super().onecmd(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
