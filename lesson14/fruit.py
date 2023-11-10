class Fruit:
    def __init__(self):
        self.sweet = True
        self.mass = 150

    def eat(self):
        self.mass = 0

class Apple(Fruit):
    def __init__(self, color):
        super().__init() 
        self.color_options = ["red", "green"]
        if color in self.color_options:
            self.color = color
        else:
            self.color = "unknown"

class Orange(Fruit):
    def __init__(self):
        super().__init()  
        self.color = "orange"
    
    def make_juice(self):
        self.juice = self.mass / 2
