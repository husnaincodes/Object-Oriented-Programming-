class Student:

    def __init__(self, name, list):
        self.name = name
        self.list = list

    def list_display(self):
        self.list.append("Python")