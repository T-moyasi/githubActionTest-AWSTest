import time

import requests


def main():
    print("test")
    while True:
        r = requests.get("https://api.bitflyer.com/v1/getticker?product_code=BTC_JPY")
        data = r.json()
        print("BTC/JPY"+data)

        time.sleep(1.0)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        pass