import requests
import json
from typing import Final

BASE_URL: Final[str] = "http://api.exchangeratesapi.io/v1/latest"
API_KEY: Final[str] = "217c1ee4194f8ca6af50afce0abf41a3"


def cached(ulr, api_key, cd = False):
    if cd:
        with open("cache.json", "r") as file:
            cur_rates = json.load(file)
            return cur_rates
    else:
        response = requests.get(url=ulr, params={"access_key": api_key})
        if response.status_code == 200:
            data = json.loads(response.text)
            for datum in data:
                if datum == "rates":
                    with open("cache.json", "w") as file:
                        json.dump(data["rates"], file, indent=4)
                        print("data cached successfully")
                    return data["rates"]
        else:
            return f"data cannot be obtained at the moment please try again later"


def get_rate(rate: str, c_rates: dict)-> float:
    rate = rate.upper()
    if rate in rates.keys():
        return round(rates.get(rate), 2)
    else:
        raise ValueError(f"{rate} not a valid currency")


def convert_currency(base: str, new: str, amount: int) -> float:
    base_rate: float = get_rate(base, rates)
    new_rate: float  = get_rate(new, rates)
    converted = base_rate / new_rate * amount
    print(f"{new}{amount} is {base}{converted:,.2f}")
    return round(converted, 2)


def currency_choices()-> str | float:
    base_currency: str = input("Enter base currency: ")
    new_currency: str = input("Enter new currency: ")
    amount_new: int = int(input("Enter amount: "))
    return convert_currency(base_currency, new_currency, amount_new)


if __name__ == '__main__':
    rates = cached(BASE_URL, API_KEY, cd=True)
    print(currency_choices())




