#!/usr/bin/python3
""" entry point of the command interpreter """
import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """ entry point hbnb Class """

    prompt = "(hbnb) "

    def do_EOF(self, line):
        """ Ctrl+d """
        return True

    def do_quit(self, arg):
        """ quit commande interpretor """
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
