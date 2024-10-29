import requests
API_KEY = "a85bde4ca143f8b0bb216f1071f902d4"

def main() -> None:

    municipality = input("Anna paikkakunta: ")
    coords_query = f"http://api.openweathermap.org/geo/1.0/direct?q={municipality}&limit=5&appid={API_KEY}"
    res = requests.get(coords_query).json()
    lat = res[0]["lat"]
    lon = res[0]["lon"]
    weather_query = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    weather_res = requests.get(weather_query).json()
    weather = weather_res["main"]["temp"]
    print(f"Lämpötila kohteessa {municipality} on {weather} Celsiusastetta")


if __name__ == '__main__':
    main()
