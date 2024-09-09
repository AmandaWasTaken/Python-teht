PI = 3.14159
def pizza_price_per_sqm(radius: float, price: float) -> float:

    area    = PI*radius**2
    radius_meters = radius/100
    area_meters = PI*radius_meters**2
    price_per_sqm = price/area_meters
    return price_per_sqm

def main():

    radius1, price1 = [float(x) for x in input("Anna pizzan 1 halkaisija ja hinta ").split()]
    radius2, price2 = [float(x) for x in input("Anna pizzan 2 halkaisija ja hinta ").split()]
    pizza1 = pizza_price_per_sqm(radius1, price1)
    pizza2 = pizza_price_per_sqm(radius2, price2)
    print("Pizza 1 on halvempi") if pizza1 < pizza2 else print("Pizza 2 on halvempi")

if __name__ == '__main__':
    main()