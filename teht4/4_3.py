
smallest: int   = 0
largest: int    = 0
while True:

    num = input("Anna luku: ")
    if int(num) > largest:
        largest = int(num)
    elif int(num) < smallest:
        smallest = int(num)
    if num == "":
        break


print(f"Suurin {largest}")
print(f"Pienin: {smallest}")