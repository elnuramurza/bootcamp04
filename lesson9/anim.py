
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Gaf-gaf!"

class Cat(Animal):
    def speak(self):
        return "Miaaa!"

class Cow(Animal):
    def speak(self):
        return "Muuu!"

class Zoo:
    def __init__(self):
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def list_animals(self):
        for animal in self.animals:
            sound = animal.speak()
            print(f"Animal: {animal.name}, Age: {animal.age} {'' if 'years' in str(animal.age) else 'years'}, Sounnd: {sound}")

dog = Dog("Baron", 3)
cat = Cat("Murzik", 2)
cow = Cow("Burenka", 5)

zoo = Zoo()
zoo.add_animal(dog)
zoo.add_animal(cat)
zoo.add_animal(cow)

zoo.list_animals()

