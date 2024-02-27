class car:

    def __init__(self, model, year, color, body, manufacturer):
        self.model = model
        self.year = year
        self.color = color
        self.type = body
        self.manufac = manufacturer


    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def get_manufac(self):
        return self.manufac

    def fullspecs(self):
        return self.model + ' ' + str(self.year) + ' ' + self.color + ' ' + self.type + ' ' + self.manufac

car1 = car("Sports", 2012, "Blue", "Small", "BMW")
car2 = car("Sedan", 2020, "Black", "Large", "Nissan")

print(car1.get_color())
print(car1.get_model())
print(car1.get_year())
print(car1.get_type())
print(car1.get_manufac())
print("This car is a",car1.fullspecs())

print(car2.get_color())
print(car2.get_model())
print(car2.get_year())
print(car2.get_type())
print(car2.get_manufac())
print("This car is a", car2.fullspecs())

# Kelly Beltran
# 02-26-24
# Problem 6: This program prints each spec of a car individually as well as a messages explaining
# all specs of each car