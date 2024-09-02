from random import randint

def dice() -> int:
        return randint(1,6)

def main() -> None:

    while True:
        x = dice()
        print(f"Saatu luku: {x}")
        if x == 6:
            break

if __name__ == '__main__':
    main()