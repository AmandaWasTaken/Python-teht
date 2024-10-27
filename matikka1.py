import numpy as np

rads = [2.493, 0.911]
degs = [137.7, 62.3]

print("Tehtävä 1:")
for i in range(2):
    print(f"{rads[i]} radiaania asteina: ")
    print(f"{np.degrees(rads[i]):.5}°")

for i in range(2):
    print(f"{degs[i]} astetta radiaaneina: ")
    print(f"{np.radians(degs[i]):.5} Rad")
    
degs = [30, 45, 60, 90, 120, 135, 150, 180, 270, 360]
arr = {}
print("\nTaulukko: ")
for i in range(10):
    arr[i] = degs[i], np.radians(degs[i])
    
for i in range(10):
    print(f"{arr[i][0]}° = {arr[i][1]:.2} Rad")

print("\nTehtävä 2: ")
print(f"Hypotenuusan pituus: {np.hypot(1.6, 2.3):.2}")

