
def main() -> None:

    sex = input("Biologinen sukupuoli?")
    hg = input("Anna hemoglobiiniarvo: ")
    hg = int(hg)

    if sex == "mies":
        if hg > 195:
            print("Arvo on liian korkea")
        elif hg < 134:
            print("Arvo on liian matala")
        else:
            print("Arvo on normaali")

    if sex == "nainen":
        if hg > 175:
            print("Arvo on liian korkea")
        elif hg < 117:
            print("Arvo on liian matala")
        else:
            print("Arvo on normaali")

if __name__ == '__main__':
    main()