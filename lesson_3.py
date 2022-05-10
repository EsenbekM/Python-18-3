class MusicPlayable:
    def play_music(self, song):
        print(f"Играет музыка {song}")

    @staticmethod
    def fn(x, y):
        print(x + y)

class Car(MusicPlayable):
    def __init__(self, year, model):
        self.__year = year
        self.__model = model

    def drive(self):
        print(f"{self.__model} driving...")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        self.__model = value

    def __str__(self):
        return f"Model: {self.model} Year: {self.year}"

    def __gt__(self, other):
        return self.year > other.year

    def __ge__(self, other):
        return self.year >= other.year

    def __eq__(self, other):
        return self.year == other.year



class FuelCar(Car):

    __gas_station = 90000

    def __init__(self, year, model, fuel_amount):
        Car.__init__(self, year, model)
        self.__fuel_amount = fuel_amount

    @staticmethod
    def fuel_type():
        print("AI-95")

    @classmethod
    def put_fuel(cls, car, amount):
        car.fuel_amount = car.fuel_amount + amount
        cls.__gas_station = cls.__gas_station - amount
        print(f"В заправке осталось {cls.__gas_station} литров топлива")


    def drive(self):
        print(f"{self.model} driving by fuel...")

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, value):
        self.__fuel_amount = value

    def info(self):
        print(f"Model: {self.model} Year: {self.year} fuel amount: {self.fuel_amount}")

    def __str__(self):
        return super(FuelCar, self).__str__() + f" fuel amount: {self.fuel_amount}"

    def __add__(self, other):
        return self.fuel_amount + other.fuel_amount



class ElectricCar(Car):
    def __init__(self, year, model, battery):
        Car.__init__(self, year, model)
        self.__battery = battery

    def drive(self):
        print(f"{self.model} driving by electricity...")

    @property
    def battery(self):
        return self.__battery

    @battery.setter
    def battery(self, value):
        self.__battery = value

    def __str__(self):
        return super(ElectricCar, self).__str__() + f" fuel amount: {self.battery}"


class HybridCar(FuelCar, ElectricCar):
    def __init__(self, year, model, fuel_amount, battery):
        ElectricCar.__init__(self, year, model, battery)
        FuelCar.__init__(self, year, model, fuel_amount)



class SmartPhone(MusicPlayable):
    pass



zhiguli = FuelCar(2022, "zhiguli", 45)
bmw = FuelCar(2022, "bmw", 55)

FuelCar.put_fuel(bmw, 50)
FuelCar.put_fuel(zhiguli, 111)
# print(zhiguli + bmw)
# print(zhiguli)
# zhiguli.drive()
FuelCar.fuel_type()
tesla = ElectricCar(2022, "Model X", 700000)
# print(tesla)
# tesla.drive()


toyota = HybridCar(2021, "Toyota Camry 75", 40, 500000)
# toyota.drive()

# print(HybridCar.mro())   # порядок разрешения методов в Python
# print(HybridCar.__mro__)

# print(zhiguli != tesla)
# toyota.play_music("Жар Жар")


# p1 = SmartPhone()
# p1.play_music("Expirience")

MusicPlayable.fn(5, 7)