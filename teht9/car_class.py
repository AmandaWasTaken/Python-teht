class Car:

    def __init__(self, register_id: str, top_speed: int):
        self.register_id = register_id
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

    def accelerate(self, speed_change: int) -> None:
        if self.current_speed + speed_change < 0:
            print("Can't go slower than 0km/h ")
            exit(1)
        if self.current_speed + speed_change > self.top_speed:
            print(f"Can't go over the car's top speed ({self.top_speed}km/h)")
            exit(1)
        self.current_speed += speed_change

    def travel(self, hours: float) -> None:
        self.distance_traveled += self.current_speed*hours

