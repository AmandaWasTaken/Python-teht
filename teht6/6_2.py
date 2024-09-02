from random import randint

def dice(sides: int) -> int:
        return randint(1,sides)

def main() -> None:

    sides = input("Anna tahkojen määrä: ")
    sides = int(sides)
    while True:
        x = dice(sides)
        print(f"Saatu luku: {x}")
        if x == sides:
            break

if __name__ == '__main__':
    main()