class Rectangle: 
    def init(self, a, b): 
     self.a = a 
     self.b = b @propert 
     def a(self):return 
     self.a @a.setter 
     def a(self, a): 
     self.a = a 
     @property def b(self): 
     return self.b 
     @b.setter def b(self, b): 
     self.b = b 
     rectangle = Rectangle(4, 3) 
     print(rectangle.a, rectangle.b)
