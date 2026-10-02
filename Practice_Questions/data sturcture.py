class Student :
    def __init__(self, name, subjects, marks, skills, information):
        self.name = name
        self.subjects = subjects      # List
        self.marks = marks            # Tuple
        self.skills = skills          # Set
        self.information = information  # Dictionary
    def display(self):
        print("Name:", self.name)

        print("Subjects:", self.subjects)

        print("Marks:", self.marks)

        print("Skills:", self.skills)

        print("Information:", self.information)

s1 = Student(
    "Husnain",
    ["Python", "Data Analytics", "OOP"],
    (85, 90, 88),
    {"Python", "Excel", "Power BI"},
    {
        "age": 19,
        "university": "ITU",
        "semester": 3
    })

s1.subjects.append("Statistics")

s1.display()