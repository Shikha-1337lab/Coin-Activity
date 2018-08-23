# importing the requests library
import requests
import json
import time

# api-endpoint
URL1 = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?sort=market_cap&limit=26&CMC_PRO_API_KEY=d583db45-0e2f-47b3-8038-c639b193aa70"

r1 = requests.get(url = URL1)
data1  = r1.json()

i=0;
while i<=25:

    name = data1['data'][i]['name']
    price = data1['data'][i]['quote']['USD']['price']
    volume = data1['data'][i]['quote']['USD']['volume_24h']
    marketcap = data1['data'][i]['quote']['USD']['market_cap']
    symbol = data1['data'][i]['symbol']
    id = data1['data'][i]['id']

    print ("----------------------------------------------")
    print (" This is the details for coin: %s" %(name))
    print ("Total cap is %s" %(marketcap))
    print ("Volume in the last 24hrs is %s" %(volume))
    print ("Price is %s" %(price))
    print ("Symbol is %s" %(symbol))



    URL2 = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?id={}&CMC_PRO_API_KEY=d583db45-0e2f-47b3-8038-c639b193aa70".format(id)
    r2 = requests.get(url = URL2)
    data2  = r2.json()

    logo = data2['data']["{}".format(id)]['logo']
    website = data2['data']["{}".format(id)]['urls']['website'][0]
    type = data2['data']["{}".format(id)]['category']

    print ("Coin logo can be found at %s" %(logo))
    print ("Coin website is %s" %(website))
    print ("Coin type is: %s" %(type))

    i = i + 1
    print ("Going to sleep for 5 seconds to avoid API throttling")
    print ("      ")
    time.sleep(5)
