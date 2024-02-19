# In a file called bitcoin.py, implement a program that:

 # Expects the user to specify as a command-line argument the number of Bitcoins,n, that they would like to buy.
# If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.
# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json,
# which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch 
# any exceptions


import sys
import requests

def get_btc_price(url, qtd ):

    try:
        if not (type(qtd) == float or type(qtd) == int):
            print('Command-line argument is not a number')
            sys.exit(1)

        response = requests.get(url)

        if response.status_code == 200:
            json_response = response.json()
            usd_rate = json_response['bpi'] ['USD'] ['rate'].replace(',', '')
            total = float(qtd) * float(usd_rate)
            return f"${total:,.4f}"

        else:
            print('Error', response.status_code)
            sys.exit(1)

    except IndexError:
        print('Missing command-line argument')
        sys.exit(1)


if __name__ == '__main__':
    url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
    qtd = float(sys.argv[1])
    print(get_btc_price(url, qtd))