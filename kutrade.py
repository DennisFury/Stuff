#run with python3, install below dependency
#pip install python-kucoin

from kucoin.client import Client

api_key = ''
api_secret = ‘’
api_passphrase = ''

client = Client(api_key, api_secret, api_passphrase)

amount = int(input('input the amount of USDT to trade with: '))
to_buy = input('input the symbol to buy: ')

order = client.create_market_order(to_buy + '-USDT', Client.SIDE_BUY, funds=amount)
