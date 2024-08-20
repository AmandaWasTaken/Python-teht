
def main() -> None:

    base    = input("Anna kanta ")
    height  = input("Anna korkeus ")
    base    = int(base)
    height  = int(height)

    print(f"Piiri: {base*2 + height*2} metriä")
    print(f"Pinta-ala: {base*height} metriä")

if __name__ == '__main__':
    main()

