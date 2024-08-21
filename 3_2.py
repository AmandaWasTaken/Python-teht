
def main() -> None:

    _class = input("Anna hyttiluokka: ")

    if _class == "LUX":
        print("LUX on parvekkeellinen hytti yläkannella.")
    elif _class == "A":
        print("A on ikkunallinen hytti autokannen yläpuolella.")
    elif _class == "B":
        print("B on ikkunaton hytti autokannen yläpuolella.")
    elif _class == "C":
        print("C on ikkunaton hytti autokannen alapuolella.")
    else:
        print(f"{_class} ei ole kelvollinen hyttiluokka!")


if __name__ == '__main__':
    main()