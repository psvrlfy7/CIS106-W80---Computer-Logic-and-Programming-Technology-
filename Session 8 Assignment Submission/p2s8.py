class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price
        self.discount_price = self.sticker_price * 0.90

    def get_discount_price(self):
        return self.discount_price

class SportCar(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.sport_wheels = 'N'
        self.sport_engine = 'N'
        self.sport_interior = 'N'

    def sport_wheels_option(self):
        if self.sport_wheels == 'Y':
            return 1000
        return 0

    def sport_engine_option(self):
        if self.sport_engine == 'Y':
            return 3000
        return 0

    def sport_interior_option(self):
        if self.sport_interior == 'Y':
            return 2000
        return 0

    def price_with_options(self):
        total = self.discount_price + self.sport_wheels_option() + self.sport_engine_option() + self.sport_interior_option()
        return total

def main():
    car = Car("Toyota", "Camry", 25000)
    print(f"Car: {car.make} {car.model}, Discount Price: ${car.get_discount_price()}")

    sport_car = SportCar("Chevrolet", "Corvette", 60000)
    sport_car.sport_wheels = 'Y'
    sport_car.sport_engine = 'Y'
    sport_car.sport_interior = 'Y'
    print(f"Sport Car: {sport_car.make} {sport_car.model}, Price with Options: ${sport_car.price_with_options()}")

main()
