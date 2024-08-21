
def main() -> None:

    luku1, luku2, luku3 = [int(x) for x in input("Anna 3 kokonaislukua: ").split()]
    luku1 = int(luku1)
    luku2 = int(luku2)
    luku3 = int(luku3)

    summa: int  = luku1 + luku2 + luku3
    tulo: int   = luku1 * luku2* luku3
    avg: float  = (luku1+luku2+luku3)/3

    print(f"Summa: {summa}\n"
          f"Tulo: {tulo}\n"
          f"Keskiarvo: {avg}")


if __name__ == '__main__':
    main()

