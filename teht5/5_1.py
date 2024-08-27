from random import randint

dice_count  = input("Anna nopppien lukumäärä: ")
dice_count  = int(dice_count)
res: int    = 0

for i in range(dice_count):
    num = randint(1, 6)
    res += num

print(f"Silmälukujen summa: {res}")



