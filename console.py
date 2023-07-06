#!/usr/bin/python3
"""Console"""


import cmd

class HBNBCommand(cmd.Cmd):
    """HBNB class"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """quit"""
        return True

    def do_EOF(self, arg):
        """EOF"""
        return True

    def emptyline(self):
        """empty line shouldn't execute anything"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
