#!/usr/bin/python3
""" entry point of the command interpreter """
import cmd
import sys
from models.base_model import BaseModel

myModels = {"BaseModel": BaseModel}


class HBNBCommand(cmd.Cmd):
    """ entry point hbnb Class """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ Ctrl+d """
        return True

    def do_quit(self, arg):
        """ quit commande interpretor """
        return True

    def emptyline(self):
        """ emptyline """
        return False

    def do_create(self, arg):
        """ create """
        if not arg:
            print("** class name missing **")
        else:
            if arg in myModels:
                obj = myModels[arg]()
                print(obj.id)
                obj.save()
            else:
                print("** class doesn't exist **")
                return

    def do_show(self, arg):
        """  """


if __name__ == '__main__':
    HBNBCommand().cmdloop()
