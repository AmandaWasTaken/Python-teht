names = {"Amanda",}

while True:
    name = input("Anna nimi: ")
    if name in names:
        print("Aiemmin syötetty nimi")
    else:
        names.add(f"{name}")
        print("Uusi nimi")
    if name == '':
        break

for name in names:
    print(name)




