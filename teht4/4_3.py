num = input("Anna luku:")
smallest = largest = num

while True:
    if num != '':
        if int(num) <= smallest:
            smallest = int(num)
            num = input("Anna luku: ")
        if int(num) >= largest:
            largest = int(num)
            num = input("Anna luku: ")
        else:
            break


