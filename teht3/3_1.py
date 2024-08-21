
def main() -> None:
    length = input("Anna kuhan pituus: ")
    length = int(length)
    if length < 37:
        print("Kuha on liian lyhyt! "
              "Heitä se takaisin järveen\n"
              f"minimipituuedsta puuttuu {37-length}cm")

if __name__ == '__main__':
    main()