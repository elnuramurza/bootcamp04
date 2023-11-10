class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def show(self):
        for i in range(self.b):
            print('*' * self.a)

figure_1 = Rectangle(7, 4)
figure_1.show()

