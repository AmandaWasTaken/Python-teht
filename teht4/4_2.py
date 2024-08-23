
while True:
    inches = input("Anna tuumamäärä: ")
    inches  = int(inches)
    if inches < 0:
        print("Negatiivinen luku havaittu, "
              "Ohjelma sulkeutuu")
        break
    print(f"Senttimetrit: {inches*2.54}")

