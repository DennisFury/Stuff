#run with python3, install below dependency
#pip install python-kucoin

from kucoin.client import Client
import time

api_key = ''
api_secret = ''
api_passphrase = ''

client = Client(api_key, api_secret, api_passphrase)

amount = int(input('input the amount of USDT to trade with: '))
to_buy = input('input the symbol to buy: ')

order = client.create_market_order(to_buy + '-USDT', Client.SIDE_BUY, funds=amount)
order_id = order.get('orderId')
print('Your Order ID = ' + order_id)
time.sleep(2)

account = client.get_accounts()

my_coin = next((key for key in account if key['currency'] == to_buy), None)
no_of_coins = float(my_coin.get('balance'))
print('Number of ' + to_buy + ' purchased: ' + str(no_of_coins))

while True:
    ticker = client.get_ticker(to_buy + '-USDT')
    price = float(ticker.get('price'))
    my_value = no_of_coins * price
    print('Value of coins in USDT: ' + str(my_value))
    time.sleep(1)
