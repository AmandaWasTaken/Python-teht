import geopy.distance
import mysql.connector

conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Salasana123',
        autocommit=True,
    )

def distance_between_airports(icao_1, icao_2) -> float:

        coords_1 = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident="{icao_1}"'
        coords_2 = f'SELECT latitude_deg, longitude_deg FROM airport WHERE ident="{icao_2}"'

        cursor = conn.cursor()
        cursor.execute(coords_1)
        res_1 = cursor.fetchall()

        cursor = conn.cursor()
        cursor.execute(coords_2)
        res_2 = cursor.fetchall()

        dist = geopy.distance.distance(res_1, res_2).km
        return dist

def main() -> None:

    icao_1, icao_2 = [x for x in input(f"Anna 2 ICAO-koodia välilyönneillä erotettuna: ").split()]
    dist = distance_between_airports(icao_1, icao_2)
    print(f"Kenttien etäisyys kilometreissä: {dist:.2f}km")

if __name__ == '__main__':
    main()