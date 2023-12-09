#!/usr/bin/env python3
"""Console Module"""

import cmd

class HBNBCommand(cmd.Cmd):
    """ command that interpreter class"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """the command that exit the program"""
        return True
    
    def do_EOF(self, arg):
        """exit the program when EOF"""
        print("")
        return True
    
    def emptyline(self):
        """execute anything"""
        pass

    def do_help(self, arg):
        """th help command"""
        cmd.Cmd.do_help(self, arg)

if __name__ == '__main__':
    HBNBCommand().cmdloop()