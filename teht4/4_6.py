import time
from random import uniform
from math import pow

start_time = time.time()
num_dots    = input("Anna pisteiden määrä ")
num_dots    = int(num_dots)
radius: int = 1
hits: int   = 0

for i in range(num_dots):
    dot_x   = uniform(-1 ,1)
    dot_y   = uniform(-1, 1)
    if pow(dot_x, 2) + pow(dot_y, 2) < 1:
        hits += 1


print(4*hits/num_dots)
    # N = num_dots, n = hits

end_time = time.time()
print(f"Aika: {end_time - start_time}")