from flask import Flask, jsonify
import mysql.connector

conn = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='projekti',
    user='root',
    password='Salasana123',
    autocommit=True,
)

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def fetch_airport(icao):

    query = f"SELECT name, municipality FROM airport WHERE ident='{icao}'"
    cursor = conn.cursor()
    cursor.execute(query)
    res = cursor.fetchone()
    cursor.close()
    conn.close()
    if not res:
        res_json = {"Error" : "Something went wrong"}
    else:
        res_json = {
            "Name": res[0],
            "municipality": res[1],
            "ICAO": icao,
            }
    return jsonify(res_json)
    if __name__ == "__main__":
        app.run(use_reloader=True, host='127.0.0.1', port=3306) 


