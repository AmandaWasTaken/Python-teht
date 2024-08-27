prime = input("Anna luku: ")
prime = int(prime)

if prime == 1 or prime == 2:
    print(f"{prime} on alkuluku")
    exit(0)


for i in range(3, prime):
    if prime % i == 0:
        print(f"{prime} ei ole alkuluku")
        exit(0)

print(f"{prime} on alkuluku")