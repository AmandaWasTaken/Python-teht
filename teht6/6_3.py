
def gallons_to_liters(gallons: float) -> float:
    return gallons * 3.785

def main() -> None:
    while True:
        gallons = input("Anna gallonamäärä: ")
        gallons = float(gallons)

        if gallons < 0:
            print("Negatiivinen määrä havaittu. Poistutaan... ")
            break
        liters = gallons_to_liters(gallons)
        print(f"{gallons} gallonaa on {liters} litraa")

if __name__ == '__main__':
    main()