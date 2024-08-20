PI: float = 3.14159

def main() -> None:

    radius = input("Anna ympyrän säde ")
    radius = int(radius)
    print(f"Ympyrän PInta-ala on {PI*radius*radius}")

if __name__ == '__main__':
    main()