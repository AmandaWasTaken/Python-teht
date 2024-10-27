class Elevator:

    def __init__(self, bottom: int, top: int):
        self.bottom = bottom
        self.top    = top
        self.current_floor = 0

    def move_up(self):
        self.current_floor += 1
        print(f"Current floor: {self.current_floor}")
        return

    def move_down(self):
        self.current_floor -= 1
        print(f"Current floor: {self.current_floor}")
        return

    def move_to_floor(self, floor):
        if floor < 0:
            print("Can't go below floor 0 ")
            return
        if floor > self.top:
            print("Can't go above the highest floor")
            return

        while self.current_floor < floor:
            self.move_up()
        while self.current_floor > floor:
            self.move_down()