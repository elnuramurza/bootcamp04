
class Sea:
    def init(self, width, height):
        self.width = width
        self.height = height
        self.field = [[" " for _ in range(width)] for _ in range(height)]

    def render(self):
        for row in self.field:
            print(" ".join(row))

class Ship:
    def init(self, x, y):
        self.is_alive = True
        self.x = x
        self.y = y

    def repr(self):
        if self.is_alive:
            return "s"
        else:
            return " "


from sea import Sea
from ship import Ship

# Инициализация игры
sea = Sea(10, 10)
ships = [Ship(3, 2), Ship(4, 6)]  # Пример создания кораблей

# Игровой цикл
while True:
    # Отображение игрового поля
    sea.render()

    # Логика игры, включая проверку попаданий и обновление статуса кораблей

    # Пример выхода из игры
    exit_game = input("Хотите выйти из игры? (y/n): ")
    if exit_game.lower() == 'y':
        break

