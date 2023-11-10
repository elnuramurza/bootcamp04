
class Dog:
    def __init__(self,size=0.8, tail=1, is_running=True):
        self.size = size
        self.tail = tail
        self.is_running = is_running

    def talk(self):
        print("gaf!")

my_dog = Dog()
baby_dog = Dog( size=0.3, tail=0.6, is_running=True)
good_dog = Dog( size=0.9, tail=2, is_running=True)

my_dog.talk()
baby_dog.talk()
good_dog.talk()
