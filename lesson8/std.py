class Student:
    def __init__(self, name, age, cuorse):
        self.name = name  
        self.age = age     
        self.cuorse = cuorse

    def get_student_info(self):
        print(f" Student: {self.name}")
        print(f"Age: {self.age} let") 
        print(f"cuorse: {self.cuorse}")
 
    def calculate_birth_year(self, current_year):
        birth_year = current_year-self.age
        print(f"god rogdenie studenta: {birth_year}")   
        

student1 = Student("Elnura", 40, 4)
student1.get_student_info()
student1.calculate_birth_year(2023)

student2 = Student("Dani", 20, 2) 
student2.get_student_info()
student2.calculate_birth_year(2023)

student3 = Student("Sonia", 25, 3) 
student3.get_student_info()
student3.calculate_birth_year(2023)

