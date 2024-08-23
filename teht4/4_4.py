from random import randint, random

num: int = randint(1,10)

while True:

    guess = int(input("Arvaa numero: "))
    if guess == num:
        print("Oikein! ")
        break
    if guess < num:
        print("Liian pieni! ")
        continue
    if guess > num:
        print("Liian iso! ")
        continue