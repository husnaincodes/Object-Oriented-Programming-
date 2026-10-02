class Student:
    def __init__(self,name, id ,age, grade):
        self.name = name
        self.id = id
        self.age = age          
        self.grade = grade
        
    def display(self):
        print("Name:", self.name)
        print("ID:", self.id)
        print("Age:", self.age)
        print("Grade:", self.grade)

s1 = Student("John", 101, 20, "A")
s1.display()

s2= Student("Alice", 102, 21, "B")
s2.display()
