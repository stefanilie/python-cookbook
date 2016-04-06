from data_structures import DataStructures
import inspect

class Interface:
    def __init__(self):
        self.objDataStructures = DataStructures()
        print("initialized Interface")
    def MethodsCount(self, chapter):
        if chapter == '1':
            return inspect.getmembers(DataStructures)
