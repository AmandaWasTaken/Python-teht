seasons = ("Kevät", "Kesä", "Syksy", "Talvi")
month = int(input("Anna kuukauden numero: "))
print(seasons[0]) if month == 1 else print(seasons[month//4])

