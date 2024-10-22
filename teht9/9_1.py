import car_class as cc

def main(args, **kwargs) -> None:

    car = cc.Car("ABC-123", 142)
    print(f"Auton rekisteritunnus: {car.register_id}\n"
          f"Auton Huippunopeus: {car.top_speed}\n"
          f"Auton tämänhetkinen nopeus: {car.current_speed}\n"
          f"Auto on kulkenut {car.distance_traveled} kilometriä")

if __name__ == '__main__':
    main(None)