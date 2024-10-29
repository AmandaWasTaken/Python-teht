class Car:

    def __init__(self, register_id: str, top_speed: int):
        self.register_id = register_id
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change: int) -> None:
        if self.current_speed + speed_change < 0:
            return
        if self.current_speed + speed_change > self.top_speed:
            # print(f"Can't go over the car's top speed ({self.top_speed}km/h)")
            return
        self.current_speed += speed_change

    def travel(self, hours: float) -> None:
        self.distance_traveled += self.current_speed*hours


class Electric(Car):

    def __init__(self, register_id: str, top_speed: int, battery_capacity: float):

        self.battery_capacity = battery_capacity
        self.register_id = register_id
        self.top_speed = top_speed
        super().__init__(register_id, top_speed)


class Combustion(Car):

    def __init__(self, register_id: str, top_speed: int, tank_size: float):

        self.tank_size = tank_size
        self.register_id = register_id
        self.top_speed = top_speed
        super().__init__(register_id, top_speed)


def main() -> None:

    cars = [Electric("ABC-15", 180, 52.5),
            Combustion("ACD-123", 165, 32.3)]

    cars[0].current_speed = 150
    cars[1].current_speed = 180

    for car in cars:
        car.travel(3)
        print(car.distance_traveled)

if __name__ == '__main__':
    main()
