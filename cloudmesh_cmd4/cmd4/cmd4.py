from __future__ import print_function

import cmd
import importlib

class DynamicClass(object):

    def add_instance_method(self, f):
        setattr(self, f.__name__, f)

    @classmethod
    def add_classmethod(cls, f):
        setattr(cls, f.__name__, f)

    def load_instancemethod(self, location):
        module_name, class_name = location.rsplit(".", 1)
        f = getattr(importlib.import_module(module_name), class_name)
        self.add_instance_method(f)

    @classmethod
    def load_classmethod(cls, location):
        module_name, class_name = location.rsplit(".", 1)
        f = getattr(importlib.import_module(module_name), class_name)
        cls.add_classmethod(f)

class CloudmeshConsole(cmd.Cmd):

    def load_instancemethod(self, location):
        module_name, class_name = location.rsplit(".", 1)
        print ("LOAD", module_name, class_name)
        f = getattr(importlib.import_module(module_name), class_name)
        self.add_instance_method(f)
    
    def add_instance_method(self, f):
        setattr(self, f.__name__, f)

    def do_gregor(self, arg):
        print ("hello gregor")
        return ""

    def do_extend(self, location):
        print ("LLL", location)
        self.load_instancemethod(location)

    def do_EOF(self, args):
        return True
    
    def do_quit(self, args):
        return True

    do_q = do_quit

        
def main():
     cmd = CloudmeshConsole()
     cmd.cmdloop()

if __name__ == "__main__":
    main()
    
