import unittest
from Lab5 import Car, Sedan, SUV, Hatchback, ElectricCar, TaxiPark, CarError
class TestCar(unittest.TestCase):
    def test_valid_car_creation(self):
        car = Sedan("Toyota", 20000, 8, 180)
        self.assertEqual(car.brand, "Toyota")
        self.assertEqual(car.price, 20000)
        self.assertEqual(car.fuel_consumption, 8)
        self.assertEqual(car.max_speed, 180)
        self.assertEqual(car.car_type(), "Седан -")

    def test_invalid_car_price(self):
        with self.assertRaises(CarError):
            Car("Toyota", -100, 8, 180)

    def test_invalid_fuel_consumption(self):
        with self.assertRaises(CarError):
            Car("Toyota", 20000, 0, 180)

    def test_invalid_max_speed(self):
        with self.assertRaises(CarError):
            Car("Toyota", 20000, 8, 0)

    def test_invalid_type_data(self):
        with self.assertRaises(CarError):
            Car("Toyota", "twenty thousand", 8, 180)

class TestElectricCar(unittest.TestCase):
    def test_valid_electric_car(self):
        ecar = ElectricCar("Tesla", 50000, 220, 75)
        self.assertEqual(ecar.car_type(), "Електромобіль")
        self.assertEqual(ecar.battery_capacity, 75)
        self.assertAlmostEqual(ecar.fuel_consumption, 0.0001)

    def test_invalid_battery(self):
        with self.assertRaises(CarError):
            ElectricCar("Tesla", 50000, 220, 0)

class TestTaxiPark(unittest.TestCase):
    def setUp(self):
        self.park = TaxiPark()
        self.car1 = Sedan("Toyota Camry", 25000, 7.5, 210)
        self.car2 = SUV("BMW X5", 50000, 10.2, 240)
        self.car3 = Hatchback("Volkswagen Golf", 20000, 6.0, 200)
        self.car4 = ElectricCar("Tesla Model 3", 45000, 225, 75)
        for car in [self.car1, self.car2, self.car3, self.car4]:
            self.park.add_car(car)

    def test_total_price(self):
        self.assertEqual(self.park.total_price(), 25000 + 50000 + 20000 + 45000)

    def test_sort_by_fuel(self):
        self.park.sort_by_fuel()
        fuel_order = [car.fuel_consumption for car in self.park.cars]
        self.assertEqual(fuel_order, sorted(fuel_order))

    def test_find_by_speed_range_valid(self):
        result = self.park.find_by_speed_range(200, 230)
        brands = [car.brand for car in result]
        self.assertIn("Volkswagen Golf", brands)
        self.assertIn("Tesla Model 3", brands)

    def test_find_by_speed_range_no_cars(self):
        with self.assertRaises(CarError):
            self.park.find_by_speed_range(10, 50)

    def test_add_non_car(self):
        with self.assertRaises(CarError):
            self.park.add_car("not a car")

if __name__ == "__main__":
    unittest.main()
