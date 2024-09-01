num = input("Anna luku")
smallest = largest = num
smallest = int(smallest)
largest = int(largest)
while True:
    num = int(input("Anna luku:"))
    if num == '':
        break
    elif int(num) > largest:
        largest = num
        continue
    elif int(num) < smallest:
        smallest = num
        continue
# ei toimi en saa toimimaan antaa olla
