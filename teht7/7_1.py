vuodenajat = ("Kevät", "Kesä", "Syksy", "Talvi")
month = int(input("Anna kuukauden numero: "))
print(vuodenajat[0]) if month == 1 else print(vuodenajat[month//4])

