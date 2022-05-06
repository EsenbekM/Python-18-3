import random

class Address:
    def __init__(self, city, street, number):
        self.__city = city
        self.__street = street
        if number <= 0:
            self.__generate_rundom_num()
            print("Wrong value for address!")
        else:
            self.__number = number

    def get_city(self):  # getter
        return self.__city

    def set_city(self, value):  # setter
        self.__city = value

    def get_street(self):
        return self.__street

    def set_street(self, value):
        if isinstance(value, str):
            if len(value) >= 50:
                print("To many symbols!")
            else:
                self.__street = value
        else:
            print("Wrong value!")

    def get_number(self):
        return self.__number

    def set_number(self, value):
        if value <= 0:
            print("Wrong value for address!")
        else:
            self.__number = value

    def __generate_rundom_num(self):
        self.__number = random.randint(1, 1000)

class Animal:
    def __init__(self, age, name, address):
        self.__age = age
        self.__name = name
        self.__address = address

    @property  # getter
    def age(self):
        return self.__age

    @age.setter # setter
    def age(self, value):
        if value <= 0:
            print("ERROR!")
        else:
            self.__age = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, value):
        self.__address = value

    def info(self):
        return f"Name: {self.__name}\nAge: {self.__age}\nCity: {self.address.get_city()}\n" \
               f"Street: {self.address.get_street()}\nHome number: {self.address.get_number()}"

    def speak(self):
        pass


# address_1 = Address(city="Kant", street="Zhyldama", number=3)
# address_1.set_city("Bishkek")
# print(address_1.get_city(), address_1.get_number(), address_1.get_street())

# cat.age = -5
# print(cat.name, cat.age)

# cat = Animal(2, "Murka", address_1)
# print(cat.info())

# a_1.set_city("Osh")
# a_1.set_street("Chui")
# print(a_1.get_street())
# print(f"{a_1.__city} {a_1.street} {a_1.number}")

class Cat(Animal):
    def __init__(self, age, name, address):
        super().__init__(age, name, address)

    def speak(self):
        print(f"{self.name} says MEOW")

class Dog(Animal):
    def __init__(self, age, name, address, commands):
        super().__init__(age, name, address)
        self.commands = commands

    def speak(self):
        print(f"{self.name} says GAV")

    def info(self):
        return super().info() + f"\nCommands: {self.commands}"

class Fish(Animal):
    def __init__(self, age, name, address):
        super().__init__(age, name, address)


    def speak(self):
        print(f"{self.name} says Nothing")

a1 = Address(city="Bish", street="Chui", number=63)
cat_tom = Cat(2, "Tom", a1)
dog_sparky = Dog(5, "Sparky", a1, ["sit", "voice"])
fish_dorri = Fish(0.1, "Dorri", a1)

lst = [cat_tom, dog_sparky, fish_dorri]

for i in lst:
    i.speak()
    print(i.info())