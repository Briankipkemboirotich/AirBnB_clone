#!/usr/bin/python3
import cmd
import sys


class HelloWorld(cmd.Cmd):
    """Simple command processor example."""
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(HBNB) '

    def do_greet(self, line):
        print("hello")

    def do_EOF(self, line):
        return True


if __name__ == '__main__':
    HelloWorld().cmdloop()
