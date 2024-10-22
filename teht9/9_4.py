import car_class as cc
from random import randint


def race(cars) -> bool:
    for car in cars:
        car.accelerate(randint(-10, 15))
        car.travel(1)
    for car in cars:
        if car.distance_traveled >= 10_000:
            return True

def main() -> None:

    cars = []
    for i in range(10):
        car = cc.Car(f"ABC-{i}", randint(100, 200))
        car.distance_traveled   = 0
        car.current_speed       = 0
        cars.insert(i, car)

    hours: int = 0
    while True:
        hours += 1
        b = race(cars)
        if b:
            break

    for car in cars:
        print(f"Rekisteritunnus: {car.register_id} - "
              f"Huippunopeus: {car.top_speed} - "
              f"Kokonaismatka: {car.distance_traveled} - "
              f"Tämänhetkinen nopeus: {car.current_speed}")
        if car.distance_traveled >= 10_000:
            print(f"{car.register_id} on voittaja!")
    print(f"\nKilpailu kesti {hours} tuntia. ")


if __name__ == '__main__':
    main()
