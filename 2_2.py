
def main() -> None:

    pi: float = 3.14159
    radius = input("Anna ympyrän säde ")
    radius = int(radius)
    print(f"Ympyrän pinta-ala on {pi*radius*radius}")

if __name__ == '__main__':
    main()