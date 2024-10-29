class Publication:

    def __init__(self, name: str):
        self.name = name


class Magazine(Publication):

    def __init__(self, reporter, name: str):
        self.reporter = reporter
        super().__init__(name)

    def print_info(self):

        print(f"Nimi: {self.name}\n"
              f"Päätoimittaja: {self.reporter}")


class Book(Publication):

    def __init__(self, author: str, name: str, n_pages: int):
        self.name = name
        self.author = author
        self.n_pages = n_pages
        super().__init__(name)

    def print_info(self):

        print(f"Nimi: {self.name}\n"
              f"Kirjailija: {self.author}\n"
              f"Sivumäärä: {self.n_pages}")


def main() -> None:

    publications = [Magazine("Aku Ankka", "Aki Hyyppä"), Book("Rosa Liksom", "Hytti n:o 6", 200)]
    publications[0].print_info()
    publications[1].print_info()

if __name__ == '__main__':
    main()

