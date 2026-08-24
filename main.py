class Automobile:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def get_description(self):
        print(f"{self.brand}, {self.model},{self.year}")

    def start_engine(self):
        print("Двигатель запущен")

    def set_year(self, new_year):  # Метод для замены атрибута
        self.year = new_year


class ElectricCar(Automobile):  # Дочерний класс
    def __init__(self, brand, model, year, battery_capacity):
        super().__init__(brand, model, year)  # Переопределение атрибута родительского класса
        self.battery_capacity = battery_capacity

    def start_engine(self):
        print("Электродвигатель запущен")

    def get_battery_info(self):
        print(f"Емкость батареи: {self.battery_capacity} кВтч")


auto1 = Automobile("bmw", "X3", "2020")
auto2 = ElectricCar("Tesla", "model X", "2022", "250")

auto1.get_description()
auto1.start_engine()

auto2.get_description()
auto2.start_engine()
auto2.get_battery_info()


class Gruzovik(Automobile):
    def __init__(self, brand, model, year, load_capacity):
        super().__init__(brand, model, year)  # Переопределение атрибута родительского класса
        self.load_capacity = load_capacity

    def get_load_info(self):
        print(f"Грузоподъемность составляет {self.load_capacity}")


auto3 = Gruzovik("Lada", "vesta", "1999", "300kg")
auto3.get_load_info()

auto1.set_year("1993")
auto1.get_description()
