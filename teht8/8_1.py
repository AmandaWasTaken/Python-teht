import mysql.connector

conn = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='Salasana123',
        autocommit=True,
    )
def fetch_airport_info(icao) -> None:

    sql = (f'SELECT name, municipality '
           f'FROM airport '
           f'WHERE ident="{icao}"')
    index = conn.cursor()
    index.execute(sql)
    res = index.fetchall()
    if index.rowcount > 0:
        for line in res:
            print(f"{line}")


def main() -> None:

    icao = input("Anna ICAO-koodi: ")
    fetch_airport_info(icao)

if __name__ == '__main__':
    main()