class Transport:

    def __init__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def change_color(self, new_color):
        self.color = new_color

    def show(self):
        print(f"Model: {self.model}\n"
              f"Year: {self.year}\n"
              f"Color: {self.color}\n")


class Rocket(Transport):

    def __init__(self, model, year, color):
        # super().__init__(model, year, color)
        Transport.__init__(self, model, year, color)


class Chair:
    def __init__(self, material, ves):
        self.material = material
        self.ves = ves


class Car(Transport):  # Чертеж

    wheels = 4  # Аттрибут класса

    def __init__(self, model, year, color, chair, penalties=0.0):  # Конструктор
        Transport.__init__(self, model, year, color)
        self.penalties = penalties
        self.chair = chair

    def drive(self, city):  # Метод (Что делать?)
        print(f"Машина {self.model}, едет в город {city}")

    def show(self):
        print(f"Model: {self.model}\n"
              f"Year: {self.year}\n"
              f"Color: {self.color}\n"
              f"Penalties: {self.penalties}\n")


def f():  # Обычная функция
    print("hello")


class Truck(Car):

    def __init__(self, model, year, color, chair, penalties, load_capacity):
        super().__init__(model, year, color, chair, penalties)
        self.load_capacity = load_capacity

    def load_cargo(self, product, weight):
        if weight <= self.load_capacity:
            print(f"Продукт {product} ({weight} kg) был успешно загружен на {self.model}")
        else:
            print(f"Я не резиновый! Максимальная грузоподъемность {self.load_capacity} kg")

    def show(self):
        print(f"Model: {self.model}\n"
              f"Year: {self.year}\n"
              f"Color: {self.color}\n"
              f"Penalties: {self.penalties}\n"
              f"Load capacity: {self.load_capacity}\n")


man_truck = Truck("Man 3", 2013, "Red", Chair("Material", 20), 1500, 2000)
man_truck.show()
man_truck.load_cargo("Яблоко", 200)
man_truck.drive("Tokio")

# chair_for_car = Chair("Skin", 50)
#
# car_mers = Car("Mersedes-Benz E220", 2003, "Black", chair_for_car, 100.5)
# car_lada = Car(model="Lada 9", year=1998, color="Red", chair=chair_for_car)


# car_mers.show()

# nasa = Rocket("Rocket M1", 2022, "White")
# nasa.show()

# car_mers.drive('Bishkek')
# car_lada.drive("Osh")


# print(car_mers) # Сыылка на объект
# print(f"{car_mers.model} {car_mers.year} {car_mers.color} {car_mers.penalties} {car_mers.wheels}")
# car_mers.color = "Blue"
# car_mers.change_color(new_color="Red")
# print(f"{car_mers.model} {car_mers.year} {car_mers.color} {car_mers.penalties} {car_lada.wheels}")
# print(f"{car_lada.model} {car_lada.year} {car_lada.color} {car_lada.penalties}")

# Car.wheels = 6  # Переопределиние аттрибута класса
#
# gelik = Car("Mers G-class", 2022, "Black", 150.0)
# # print(f"{gelik.model} {gelik.year} {gelik.color} {gelik.penalties} {gelik.wheels}")
# gelik.show()
# car_lada.show()
# car_mers.show()
