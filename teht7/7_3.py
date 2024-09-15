lentoasemat = {}

while True:
    action = input("Valitse 1 jos haluat syöttää uuden aseman \n"
                   "Valitse 2 jos haluat hakea asemaa \n"
                   "Valitse mitä vain muuta lopettaaksesi ")
    if action == '1':
        new_station_code, new_station_name = [x for x in input("Syötä uuden aseman ICAO-koodi ja nimi ").split()]
        lentoasemat[new_station_code] = new_station_name
    elif action == '2':
        code_to_fetch = input("Anna haettavan aseman ICAO-koodi")

        try:
            print(f"Koodilla löytyi seuraava asema: {lentoasemat[code_to_fetch]}")
        except KeyError:
            print(f"Koodilla {code_to_fetch} ei löytynyt asemaa! ")

    else:
        break

print("Kaikki lentoasemat: ")
for i in lentoasemat:
    print(lentoasemat[i])


