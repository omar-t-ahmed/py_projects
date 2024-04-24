import requests

def fetch_currency_rates(base_currency, date='latest'):
    url = f"https://cdn.jsdelivr.net/npm/@fawazahmed0/currency-api@{date}/v1/currencies/{base_currency}.json"
    fallback_url = f"https://{date}.currency-api.pages.dev/v1/currencies/{base_currency}.json"
    try:
        response = requests.get(url)
        if response.status_code != 200:
            response = requests.get(fallback_url)
        data = response.json()
        return data['rates']
    except Exception as e:
        print(f"Failed to fetch currency rates: {e}")
        return None

def get_exchange_rate(base_currency, target_currency):
    rates = {
        'USD': 1.0,
        'EUR': 0.95,
        'GBP': 0.82,
        'JPY': 133.5
    }
    try:
        usd_to_base_rate = 1 / rates[base_currency]
        base_to_target_rate = usd_to_base_rate * rates[target_currency]
    except KeyError:
        raise ValueError("One or both specified currencies are not supported.")
    return base_to_target_rate

def convert_currency(amount, base_currency, target_currency):
    try:
        rate = get_exchange_rate(base_currency, target_currency)
    except ValueError as e:
        print(e)
        return None
    return amount * rate

def main():
    try:
        amount = float(input("Enter the amount to convert: "))
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return
    
    base_currency = input("Enter the base currency (USD, EUR, GBP, JPY): ")
    target_currency = input("Enter the target currency (USD, EUR, GBP, JPY): ")

    if base_currency not in ['USD', 'EUR', 'GBP', 'JPY'] or target_currency not in ['USD', 'EUR', 'GBP', 'JPY']:
        print("Invalid currency.")
        return

    converted_amount = convert_currency(amount, base_currency, target_currency)
    if converted_amount is not None:
        print(f"{amount} {base_currency} is equal to {converted_amount:.2f} {target_currency}")

if __name__ == "__main__":
    main()