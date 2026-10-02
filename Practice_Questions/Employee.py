class Employee:

    def __init__(self,name,id,age,salary,list):
        self.name = name
        self.id = id
        self.age = age
        self.salary = salary
        self.list = list

    def display(self):

        print("Name:", self.name)
        print("ID:", self.id)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Languages:", self.list)   

s1 = Employee("John", 101, 20, 50000, ["Python", "Java"])
s1.display()
    
s2 = Employee("Alice", 102, 21, 60000, ["C++", "JavaScript"])
s2.display()