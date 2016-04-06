from interface import Interface
import sys

class Menu:
    def __init__(self):
        self.objInterface = Interface()
        self.intro = "Python Cookbook code examples"
        self.description = "\nThis code has been written while learning Python 3."
        self.chapter = "\nPlease choose chapter. [1-15]:"
        self.section = "\nPlease choose section for "

        print(self.intro, self.description)
        chapter = input(self.chapter)
        # Why 25? Well, there are 25 default methods like __init__ for each class.
        section = input(self.section + chapter + '. [1-'+str(len(self.objInterface.MethodsCount(chapter))-25) + ']: ')
        getattr(self.objInterface.objDataStructures, "section%s_%s" % (chapter, section))()


menu = Menu();
