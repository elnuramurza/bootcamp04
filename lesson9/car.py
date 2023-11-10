class Car:
    def __init__(self, brand, year, color):
        self.brand = brand
        self.year = year
        self.color = color
        self.horsepower = 85

    def get_auto(self):
        return f"marka: {self.brand}, year: {self.year}, color: {self.color}"

    def get_year(self):
        current_year = 2023  
        age = current_year - self.year
        return f"year auto: {age} year"

    def add_horsepower(self):
        if self.brand in ["Mers", "Bmw", "Poshe"]:
            self.horsepower += 40
        else:
            self.horsepower += 20

bmw = Car ("Bmw", 2020, "black")
print("marka:", bmw.brand)
print("year:", bmw.year)
print("color:", bmw.color)

print(bmw.get_auto())
print(bmw.get_year())
print("horsepower:", bmw.horsepower)

mercedes = Car("Mers", 2019, "silver")
print(mercedes.get_auto())
print(mercedes.get_year())
print("horsepower:", mercedes.horsepower)

porsche = Car("Poshe", 2022, "red")
print(porsche.get_auto())
print(porsche.get_year())
print("horsepower:", porsche.horsepower)


