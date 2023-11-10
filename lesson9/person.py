class Person:
    def __init__(self,name,age):
        self.name = name 
        self.age = age
    def introduce(self):
        return f"My name is {self.name} and me {self.age} years."  
        from person import Person
Person
person1 = Person("Roza",30)
person2 = Person("Alim",25)
print(person1.introduce())
print(person2.introduce())