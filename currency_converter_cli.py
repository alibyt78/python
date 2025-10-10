import requests

API_URL = 'https://api.exchangerate-api.com/v4/latest/'

def convert_currency(base, target, amount):
    response = requests.get(API_URL + base)
    data = response.json()
    rate = data['rates'][target]
    return amount * rate

if __name__ == "__main__":
    base = input("Base currency: ").upper()
    target = input("Target currency: ").upper()
    amount = float(input("Amount: "))
    result = convert_currency(base, target, amount)
    print(f"{amount} {base} = {result:.2f} {target}")
