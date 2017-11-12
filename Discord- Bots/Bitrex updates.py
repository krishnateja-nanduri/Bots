import discord
import asyncio
import random
import requests
import datetime

client = discord.Client()

async def get_bittrex_updates():
    coins = [ 'BTC-LTC', 'BTC-DOGE', 'BTC-VTC', 'BTC-PPC', 'BTC-FTC', 'BTC-RDD', 'BTC-VIB', 'ETH-VIB','BTC-RCN', 'ETH-RCN', 'BTC-NXT','BTC-POT', 'BTC-DASH', 'BTC-POT', 'BTC-BLK', 'BTC-EMC2', 'BTC-XMY', 'BTC-AUR', 'BTC-EFL', 'BTC-GLD', 'BTC-SLR', 'BTC-PTC', 'BTC-GRS', 'BTC-NLG', 'BTC-RBY', 'BTC-XWC', 'BTC-MONA', 'BTC-THC', 'BTC-ENRG', 'BTC-ERC', 'BTC-VRC', 'BTC-CURE', 'BTC-XMR', 'BTC-CLOAK', 'BTC-START', 'BTC-KORE', 'BTC-XDN', 'BTC-TRUST', 'BTC-NAV', 'BTC-XST', 'BTC-BTCD', 'BTC-VIA', 'BTC-PINK', 'BTC-IOC', 'BTC-CANN', 'BTC-SYS', 'BTC-NEOS', 'BTC-DGB', 'BTC-BURST', 'BTC-EXCL', 'BTC-SWIFT', 'BTC-DOPE', 'BTC-BLOCK', 'BTC-ABY', 'BTC-BYC', 'BTC-XMG', 'BTC-BLITZ', 'BTC-BAY', 'BTC-BTS', 'BTC-FAIR', 'BTC-SPR', 'BTC-VTR', 'BTC-XRP', 'BTC-GAME', 'BTC-COVAL', 'BTC-NXS', 'BTC-XCP', 'BTC-BITB', 'BTC-GEO', 'BTC-FLDC', 'BTC-GRC', 'BTC-FLO', 'BTC-NBT', 'BTC-MUE', 'BTC-XEM', 'BTC-CLAM', 'BTC-DMD', 'BTC-GAM', 'BTC-SPHR', 'BTC-OK', 'BTC-SNRG', 'BTC-PKB', 'BTC-CPC', 'BTC-AEON', 'BTC-ETH', 'BTC-GCR', 'BTC-TX', 'BTC-BCY', 'BTC-EXP', 'BTC-INFX', 'BTC-OMNI', 'BTC-AMP', 'BTC-AGRS', 'BTC-XLM', 'USDT-BTC', 'BTC-CLUB', 'BTC-VOX', 'BTC-EMC', 'BTC-FCT', 'BTC-MAID', 'BTC-EGC', 'BTC-SLS', 'BTC-RADS', 'BTC-DCR', 'BTC-SAFEX', 'BTC-BSD', 'BTC-XVG', 'BTC-PIVX', 'BTC-XVC', 'BTC-MEME', 'BTC-STEEM', 'BTC-2GIVE', 'BTC-LSK', 'BTC-PDC', 'BTC-BRK', 'BTC-DGD', 'ETH-DGD', 'BTC-WAVES', 'BTC-RISE', 'BTC-LBC', 'BTC-SBD', 'BTC-BRX', 'BTC-ETC', 'ETH-ETC', 'BTC-STRAT', 'BTC-UNB', 'BTC-SYNX', 'BTC-TRIG', 'BTC-EBST', 'BTC-VRM', 'BTC-SEQ', 'BTC-XAUR', 'BTC-SNGLS', 'BTC-REP', 'BTC-SHIFT', 'BTC-ARDR', 'BTC-XZC', 'BTC-NEO', 'BTC-ZEC', 'BTC-ZCL', 'BTC-IOP', 'BTC-GOLOS', 'BTC-UBQ', 'BTC-KMD', 'BTC-GBG', 'BTC-SIB', 'BTC-ION', 'BTC-LMC', 'BTC-QWARK', 'BTC-CRW', 'BTC-SWT', 'BTC-TIME', 'BTC-MLN', 'BTC-ARK', 'BTC-DYN', 'BTC-TKS', 'BTC-MUSIC', 'BTC-DTB', 'BTC-INCNT', 'BTC-GBYTE', 'BTC-GNT', 'BTC-NXC', 'BTC-EDG', 'BTC-LGD', 'BTC-TRST', 'ETH-GNT', 'ETH-REP', 'USDT-ETH', 'ETH-WINGS', 'BTC-WINGS', 'BTC-RLC', 'BTC-GNO', 'BTC-GUP', 'BTC-LUN', 'ETH-GUP', 'ETH-RLC', 'ETH-LUN', 'ETH-SNGLS', 'ETH-GNO', 'BTC-APX', 'BTC-TKN', 'ETH-TKN', 'BTC-HMQ', 'ETH-HMQ', 'BTC-ANT', 'ETH-TRST', 'ETH-ANT', 'BTC-SC', 'ETH-BAT', 'BTC-BAT', 'BTC-ZEN', 'BTC-1ST', 'BTC-QRL', 'ETH-1ST', 'ETH-QRL', 'BTC-CRB', 'ETH-CRB', 'ETH-LGD', 'BTC-PTOY', 'ETH-PTOY', 'BTC-MYST', 'ETH-MYST', 'BTC-CFI', 'ETH-CFI', 'BTC-BNT', 'ETH-BNT', 'BTC-NMR', 'ETH-NMR', 'ETH-TIME', 'ETH-LTC', 'ETH-XRP', 'BTC-SNT', 'ETH-SNT', 'BTC-DCT', 'BTC-XEL', 'BTC-MCO', 'ETH-MCO', 'BTC-ADT', 'ETH-ADT', 'BTC-FUN', 'ETH-FUN', 'BTC-PAY', 'ETH-PAY', 'BTC-MTL', 'ETH-MTL', 'BTC-STORJ', 'ETH-STORJ', 'BTC-ADX', 'ETH-ADX', 'ETH-DASH', 'ETH-SC', 'ETH-ZEC', 'USDT-ZEC', 'USDT-LTC', 'USDT-ETC', 'USDT-XRP', 'BTC-OMG', 'ETH-OMG', 'BTC-CVC', 'ETH-CVC', 'BTC-PART', 'BTC-QTUM', 'ETH-QTUM', 'ETH-XMR', 'ETH-XEM', 'ETH-XLM', 'ETH-NEO', 'USDT-XMR', 'USDT-DASH', 'ETH-BCC', 'USDT-BCC', 'BTC-BCC', 'BTC-DNT', 'ETH-DNT', 'USDT-NEO', 'ETH-WAVES', 'ETH-STRAT', 'ETH-DGB', 'ETH-FCT', 'ETH-BTS', 'USDT-OMG', 'BTC-ADA', 'BTC-MANA', 'ETH-MANA', 'BTC-SALT', 'ETH-SALT', 'BTC-TIX', 'ETH-TIX']
    bittrex_url = 'https://bittrex.com/api/v1.1/public/getmarkets'
    await client.wait_until_ready()
    while not client.is_closed:
        channel1 = client.get_channel("Channel ID here")
        channel2 = client.get_channel("Channel ID here")
        while(True):
               time.sleep(1)
               present_time = datetime.datetime.now()
               await client.send_message(channel1, 'BITTREX Checking at: {}'.format(present_time))
               res = requests.get(bittrex_url)
               if res.status_code == requests.codes.ok:
                       response = res.json()
                       if response.get('success'):
                               for coin in response.get('result'):
                                       marketName = coin.get('MarketName')
                                       if marketName not in coins:
                                               coins.append(marketName)
                                               await client.send_message(channel2,'Found new coin: {}'.format(marketName))
                                               newcoin = coin.get('MarketName')
                                               coincreated = coin.get('Created')
                                               await client.send_message(channel2, 'Coin {}'.format(newcoin) + ' added on {}'.format(coincreated))
                                               await asyncio.sleep(1)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print("ID:")
    print(client.user.id)
    print('------')
    print(datetime.datetime.now())




client.loop.create_task(get_bittrex_updates())
client.run("Your Token here")
