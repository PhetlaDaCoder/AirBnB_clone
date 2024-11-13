#!/usr/bin/python3

import cmd


class HBNBCommand(cmd.Cmd):

    prompt = '(hbnb)'

    def do_quit(self, arg):
        """Quit command to exit the program."""
        print("Exiting... Goodbye!")
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program (CTrl+D)."""
        print("Exiting... Goodbye!")
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
