from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route('/alkuluku/<int:num>', methods=['GET'])
def is_prime(num: int):
    is_prime: bool = True 
    if num <= 1:
        is_prime = False
    else:
        for i in range(2, int(num/2)):
            if num % i == 0:
                is_prime = False
                break

    res = {"Number": num, "isPrime": is_prime}
    res = jsonify(res)
    return res

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)
