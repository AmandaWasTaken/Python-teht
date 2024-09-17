import mysql.connector

conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Salasana123',
        autocommit=True,
    )
def fetch_all_airports(country_code: str) -> None:

    sql_small = f'SELECT type FROM airport WHERE iso_country="{country_code}"'
    cursor = conn.cursor()
    cursor.execute(sql_small)
    res = cursor.fetchall()

    small = medium = heli = closed = 0
    for line in res:
        if line.__contains__("closed"):
            closed += 1
        elif line.__contains__("small_airport"):
            small += 1
        elif line.__contains__("medium_airport"):
            medium += 1
        elif line.__contains__("heliport"):
            heli += 1
    print(f"Country: {country_code}")
    print(f"Small airports: {small}\nMedium airports: {medium}\nHeliports: {heli}\nClosed ports: {closed}")
    print(f"Total airports in {country_code}: {small+medium+heli+closed}")

def main() -> None:

    country_code = input("Anna maakoodi: ")
    fetch_all_airports(country_code)

if __name__ == '__main__':
    main()