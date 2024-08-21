
def main() -> None:

    year = input("Anna vuosiluku: ")
    year = int(year)

    if year % 4 == 0 and year % 100 != 0:
        print("Karkausvuosi")
    elif year % 100 == 0 and year % 4 == 0 and year % 400 == 0:
        print("Karkausvuosi")
    else:
        print("Ei karkausvuosi")

if __name__ == '__main__':
    main()
