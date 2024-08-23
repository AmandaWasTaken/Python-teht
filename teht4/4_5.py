USERNAME: str = "python"
PASSWORD: str = "rules"


guesses: int = 5

while guesses >= 0:
    guess_un = input("Anna käyttäjänimi: ")
    guess_pw = input("Anna salasana: ")
    if guess_pw != PASSWORD or guess_un != USERNAME:
        guesses -= 1
        print(f"Käyttäjänimi tai salasana väärin! "
              f"{guesses} yritystä jäljellä")
    else:
        print("Tervetuloa")
        break
    if guesses == 0:
        print("Pääsy evätty")
        break