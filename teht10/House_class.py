import Elevator_class as Ec

class House:

    def __init__(self, bottom:int, top:int, n_elevators:int):
        self.top    = top
        self.bottom = bottom
        self.n_elevators = n_elevators
        self.elevators = []
        for i in range(n_elevators):
            elevator = Ec.Elevator(bottom, top)
            self.elevators.append(elevator)

    def use_elevator(self, elevator_n, floor: int):
        elev = self.elevators[elevator_n-1]
        elev.move_to_floor(floor)

    def fire_emergency(self):
        print("PALOHÄLYTYS!!!!")
        for e in self.elevators:
            e.move_to_floor(0)
