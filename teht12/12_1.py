import requests

def main() -> None:

    query = "https://api.chucknorris.io/jokes/random"
    res = requests.get(query)
    if res.status_code == 200:
        res = res.json()
        print(res["value"])
    else:
        print(f"Something went wrong! ({res.status_code})")

if __name__ == '__main__':
    main()
