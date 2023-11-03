import cryptocompare
import os

while True:
    os.system('cls; clear')
    print("*******************************************************")
    print("***                  CRYPTO TRACKER                 ***")
    print("***                     Ver. 1.0                    ***")
    print("***                                                 ***")
    print("***                  Type a number:                 ***")
    print("***                                                 ***")
    print("***   Bitcoin (BTC) = 1        Ethereum (ETH) = 2   ***")
    print("***                                                 ***")
    print("***   Tether (USDT) = 3        USD Coin (USDC) = 4  ***")
    print("***                                                 ***")
    print("***   BNB (BNB) = 5            XRP (XRP) = 6        ***")
    print("***                                                 ***")
    print("***                    Exit = 7                     ***")
    print("*******************************************************\n")
    valor = input(": ")
    def crypto(valor):
        return {
            '1': 'BTC',
            '2': 'ETH',
            '3': 'USDT',
            '4': 'USDC',
            '5': 'BNB',
            '6': 'XRP',
            '7': 'Sair',
        }.get(valor, 'default')
    nome_crypto = crypto(valor)
    if nome_crypto == 'Sair':
        break
    elif nome_crypto == 'default':
        continue
    price = cryptocompare.get_price(nome_crypto, currency='USD')
    print(f'The current price of {nome_crypto} is {price[nome_crypto]['USD']} USD')
    valor = input("Press any key to continue: ")