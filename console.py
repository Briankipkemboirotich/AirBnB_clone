#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """Simple command processor example."""
    intro = 'Welcome to the turtle shell.   Type help or ? to list commands.\n'
    prompt = '(hbnb) '

    def do_create(self, arg):
        """ reates a new instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
            return

        if arg not in ["BaseModel"]:
            print("** class doesn't exist **")
            return

        obj = BaseModel()
        obj.save()
        print(obj.id)

    def do_show(self,arg):
        """ rints the string representation of an instance """
        arr=arg.partition(" ")
        name=arr[0]
        id=arr[2]
        if not name:
            print("** class name missing **")
            return

        if name  not in ["BaseModel"]:
            print("* class doesn't exist **")
            return
        
        if not id:
            print("** instance id missing **")
            return

        key = name + "." + id
        try:
            print(storage.all()[key])
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id"""
        arr = args.partition(" ")
        name = arr[0]
        id =  arr[2]
        if not name:
            print("** class name missing **")
            return
        if name not in ["BaseModel"]:
            print("** class doesn't exist **")
            return
        
        if not id:
            print("** instance id missing **")
            return
        key = name + "." + id
        try:
            storage.delete(key)
            storage.save()
        except KeyError:
            print("** no instance found **")
    
    def do_all(self,arg):
        "Prints all string representation of all instances based "
        obj_list =[]
        if arg:
            if arg not in ["BaseModel"]:
                print("** class doesn't exist **")
                return
            for v in storage.all().items():
                    obj_list.append(str(v))
            
        else:
            for v in storage.all().items():
                    obj_list.append(str(v))
        
        print(obj_list)
    
    def do_update(self,args):
        """ Updates an instance based on the class name and id by adding or updating"""
        args = args.partition(" ")
        print(args)
        if args[0]:
            c_name = args[0]
        else:
            print("** class name missing **")
            return
        if c_name not in ["BaseModel"]: 
            print("** class doesn't exist **")
            return

        args = args[2].partition(" ")
        if args[0]:
            c_id = args[0]

        else:  # id not present
            print("** instance id missing **")
            return
        key = c_name + "." + c_id

        if key not in storage.all():
            print("** no instance found **")
            return
        
        
        
    def do_EOF(self, line):
        return True

    def do_quit(self, arg):
        """ Exit the console and commit all changes"""
        return True

    def emptyline(self):
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
