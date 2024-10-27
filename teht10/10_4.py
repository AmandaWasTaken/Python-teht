from random import randint
import car_class as cc

class Race:

    def __init__(self, name: str, kms: int, cars: []):
        self.name   = name
        self.kms    = kms
        self.cars   = cars

    def race_over(self) -> bool:

        for car in self.cars:
            if car.distance_traveled >= self.kms:
                return True
        return False


    def hour_passes(self):

        for car in self.cars:
            car.accelerate(randint(-15, 10))
            car.travel(1)
            self.print_stats()

    def print_stats(self):

        for car in self.cars:
            print(f"Auto: {car.register_id}\n"
                  f"Kuljettu matka: {car.distance_traveled}\n"
                  f"Tämänhetkinen nopeus: {car.current_speed}\n")


def main():

    cars = []
    for i in range(10):
        car = cc.Car(f"ABC-{i}", 150)
        car.distance_traveled   = 0
        car.current_speed       = 0
        cars.insert(i, car)

    race = Race("Suuri Romuralli", 8000, cars)
    while not race.race_over():
        race.hour_passes()

    race.print_stats()
    for car in cars:
        if car.distance_traveled > race.kms:
            print(f"Auto {car.register_id} Voittaa!\n")


if __name__ == '__main__':
    main()

