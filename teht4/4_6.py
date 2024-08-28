from random import random
import math

pi: float   = 3.14159
num_dots    = input("Anna pisteiden määrä ")
num_dots    = int(num_dots)
radius: int = 1
area: float = pi/4

for i in range(num_dots):
    dot_x = random()
    dot_y = random()
    if (math.pow(dot_x, 2) + math.pow(dot_y, 2)) < 1:
        print(f"{dot_x} {dot_y}")

