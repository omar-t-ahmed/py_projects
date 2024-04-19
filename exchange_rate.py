def get_exchange_rate(base_currency, target_currency):
    rates = {
        'USD': 1.0,
        'EUR': 0.95,
        'GBP': 0.82,
        'JPY': 133.5
    }
    usd_to_base_rate = 1 / rates[base_currency]
    base_to_target_rate = usd_to_base_rate * rates[target_currency]
    return base_to_target_rate

def convert_currency(amount, base_currency, target_currency):
    rate = get_exchange_rate(base_currency, target_currency)
    return amount * rate