GRAMMA      = 1
LUOTI       = 13.3 * GRAMMA
NAULA       = 32 * LUOTI
LEIVISKA    = 20 * NAULA

def main() -> None:

    leiv = input("Anna leiviskät: ")
    naulat = input("Anna naulat: ")
    luodit = input("Anna luodit: ")

    leiv = float(leiv)
    naulat = float(naulat)
    luodit = float(luodit)

    kilos = int(luodit*LUOTI + naulat*NAULA + leiv*LEIVISKA)/1000
    print(f"Massa: {kilos} kilogrammaa")

if __name__ == '__main__':
    main()