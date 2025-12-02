# currency_converter.py
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
from forex_python.converter import RatesNotAvailableError

def convert_currency(amount, from_currency, to_currency):
    c = CurrencyRates()
    try:
        rate = c.get_rate(from_currency.upper(), to_currency.upper())
        converted_amount = round(amount * rate, 2)
        return f"{amount} {from_currency.upper()} = {converted_amount} {to_currency.upper()}"
    except RatesNotAvailableError:
        return "Currency rates not available at the moment."
    except Exception as e:
        return f"Error: {str(e)}"

def convert_bitcoin(amount, currency):
    btc = BtcConverter()
    try:
        btc_value = btc.get_latest_price(currency.upper())
        converted_amount = round(amount * btc_value, 2)
        return f"{amount} BTC = {converted_amount} {currency.upper()}"
    except Exception as e:
        return f"Error: {str(e)}"

# Example usage
if __name__ == "__main__":
    print(convert_currency(100, 'USD', 'INR'))  
    print(convert_bitcoin(0.1, 'USD'))          
