class Student:
    def __init__(self,name):
        self.name = name
        self.subjects = []  # Initialize an empty list for subjects
        self.marks = ()
        self.skills = set()
        self.information = {}

    def add_subject(self, subject):
        self.subjects.append(subject)

    def add_marks(self, marks):
        self.marks = marks
    def add_skills(self, skills):
        self.skills = skills
    def add_information(self, key, value ):
        self.information[key]= value
    def display(self):
        print("Name:", self.name)
        print("Subjects:", self.subjects)
        print("Marks:", self.marks)
        print("Skills:", self.skills)
        print("Information:", self.information) 

s1 = Student("Husnain")
s1.add_subject("Python")    
s1.add_subject("Data Analytics")
s1.add_subject("OOP")

s1.add_marks((85, 90, 88))
s1.add_skills({"Python", "Excel", "Power BI"})
s1.add_information("age", 19)   
s1.add_information("university", "ITU")
s1.add_information("semester", 3)

s1.display()
s2 = Student("Ali")
s2.add_subject("Statistics")    
s2.add_subject("Machine Learning")
s2.add_marks((92, 87, 95))  
s2.add_skills({"Python", "R", "SQL"})
s2.add_information("age", 20)   
s2.add_information("university", "NED")
s2.add_information("semester", 4)   
s2.display()