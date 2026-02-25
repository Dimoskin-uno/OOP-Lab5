class CarError(Exception):
    pass
class Car:
    def __init__(self, brand, price, fuel_consumption, max_speed):
        try:
            self.price = float(price)
            self.fuel_consumption = float(fuel_consumption)
            self.max_speed = int(max_speed)

            if price < 0:
                raise CarError("Вартість автомобіля не може бути від’ємною.")
            if fuel_consumption <= 0:
                raise CarError("Витрати палива повинні бути більші за 0.")
            if max_speed <= 0:
                raise CarError("Швидкість повинна бути більшою за 0.")

            self.brand = brand

        except ValueError:
            raise CarError("Невірний тип даних при створенні автомобіля.")

    def car_type(self):
        pass

    def __str__(self):
        return (f"{self.car_type()} Марка: {self.brand}, "
                f"Ціна: {self.price}, Витрати палива: {self.fuel_consumption}, "
                f"Швидкість: {self.max_speed}")

class Sedan(Car):
    def car_type(self):
        return "Седан -"

class SUV(Car):
    def car_type(self):
        return "Позашляховик -"

class Hatchback(Car):
    def car_type(self):
        return "Хетчбек -"

class ElectricCar(Car):
    def __init__(self, brand, price, max_speed, battery_capacity):
        if battery_capacity <= 0:
            raise CarError("Ємність батареї повинна бути більшою за 0.")
        super().__init__(brand, price, 0.0001, max_speed)  # майже 0
        self.battery_capacity = battery_capacity

    def car_type(self):
        return "Електромобіль"

    def __str__(self):
        return super().__str__() + f", Батарея: {self.battery_capacity} кВт/год"

class TaxiPark:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        if not isinstance(car, Car):
            raise CarError("Можна додавати лише об’єкти типу Car.")
        self.cars.append(car)

    def total_price(self):
        try:
            return sum(car.price for car in self.cars)
        except Exception:
            raise CarError("Помилка підрахунку вартості автопарку.")

    def sort_by_fuel(self):
        try:
            self.cars.sort(key=lambda car: car.fuel_consumption)
        except Exception:
            raise CarError("Помилка сортування автомобілів.")

    def find_by_speed_range(self, min_speed, max_speed):
        if min_speed < 0 or max_speed < 0:
            raise CarError("Швидкість не може бути від’ємною.")
        if min_speed > max_speed:
            raise CarError("Мінімальна швидкість більша за максимальну.")

        result = [car for car in self.cars
                  if min_speed <= car.max_speed <= max_speed]

        if not result:
            raise CarError("Автомобілі у заданому діапазоні не знайдені.")
        return result

    def show_all(self):
        if not self.cars:
            print("Таксопарк порожній.")
        for car in self.cars:
            print(car)

class Program:
    def execute():
        try:
            park = TaxiPark()
            park.add_car(Sedan("Toyota Camry", 25000, 7.5, 210))
            park.add_car(SUV("BMW X5", 50000, 10.2, 240))
            park.add_car(Hatchback("Volkswagen Golf", 20000, 6.0, 200))
            park.add_car(ElectricCar("Tesla Model 3", 45000, 225, 75))

            print("Автомобілі таксопарку:")
            park.show_all()

            print("\nЗагальна вартість автопарку:")
            print(park.total_price())

            print("\nСортування за витратами палива:")
            park.sort_by_fuel()
            park.show_all()

            print("\nПошук авто (швидкість 200-230):")
            cars = park.find_by_speed_range(200, 230)
            for car in cars:
                print(car)

        except CarError as e:
            print("Помилка:", e)
        except Exception as e:
            print("Невідома помилка:", e)
if __name__ == "__main__":
    Program.execute()
