#!/usr/bin/python3
"""Console"""


import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNB class"""
    prompt = "(hbnb)"
    all_classes = {"BaseModel": BaseModel, "User": User, "State": State,
                   "City": City, "Amenity": Amenity,
                   "Review": Review, 'Place': Place}

    def do_quit(self, arg):
        """quit"""
        return True

    def do_EOF(self, arg):
        """EOF"""
        return True

    def do_create(self, arg):
        """This instace creates a new class"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.all_classes:
            print("** class doesn't exist **")
        else:
            instance = eval(arg)()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if len(line) == 0:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        elif len(args) < 2:
            print("** instance id missing**")
            return
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            names = f"{args[0]}.{args[1]}"
            print(storage.all()[names])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""

        args = arg.split()
        if arg == "":
            print("** class name missing **")
        elif args[0] not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        else:
            names = f"{args[0]}.{args[1]}"
            storage.all().pop(names)
            storage.save()

    def do_all(self, line):
        """Print string representation of all instances based on class name"""
        if len(line) == 0:
            print("** class name missing **")
            return

        class_name = line
        if class_name not in self.all_classes:
            print("** class doesn't exist **")
            return

        instances = []
        for key, value in storage.all().items():
            if class_name == key.split('.')[0]:
                instances.append(str(value))
        print(instances)

    def do_update(self, arg):
        """
        Updates an instance based on the
        class name and id
        by adding or updating attribute
        """
        args = arg.split()
        if not arg:
            print("** class name missing **")
        elif args[0] not in self.all_classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif f"{args[0]}.{args[1]}" not in storage.all():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            print("** value missing **")
        else:
            name = f"{args[0]}.{args[1]}"
            obj = storage.all()[name]
            setattr(obj, args[2], args[3])
            obj.save()

    def emptyline(self):
        """empty line shouldn't execute anything"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
