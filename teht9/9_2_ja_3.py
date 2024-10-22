import car_class as cc


def main() -> None:

    car = cc.Car("ABC-123", 180)
    car.accelerate(30)
    car.accelerate(70)
    car.accelerate(50)
    print(f"Tämänhetkinen nopeus: {car.current_speed}km/h")
    car.accelerate(-150)

    # Tehtävä 3. Tuntui turhalta tehdä erillinen tiedosto muutaman koodirivin vuoksi
    car.distance_traveled = 2000
    car.current_speed = 60
    car.travel(1.5)
    print(car.distance_traveled)


if __name__ == '__main__':
    main()


