import mysql.connector

def fetch_airport(icao: str):
    sql = f"SELECT ident FROM airport where icao='{icao}'"
    print(sql)
    kursori = conn.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Päivää! Olen {rivi[2]} {rivi[1]}. Palkkani on {rivi[3]} euroa kuussa.")
    return

conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='Salasana123',
    autocommit=True,
)

foo = input("Anna sukunimi: ")
fetch_airport(foo)