from .models  import Coins
import json
import time
import requests

def insertDB(request): # this is bulk load of data to Database - dont call this function repeatedly
    URL1 = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?sort=market_cap&limit=26&CMC_PRO_API_KEY=d583db45-0e2f-47b3-8038-c639b193aa70"

    r1 = requests.get(url = URL1)
    data1  = r1.json()
    #
    # conn = psycopg2.connect(host=dbserver,database=dbname)
    # cur = conn.cursor()

    i=0;
    while i<=5:

        name_1 = data1['data'][i]['name']
        price = data1['data'][i]['quote']['USD']['price']
        volume = data1['data'][i]['quote']['USD']['volume_24h']
        marketcap_1 = data1['data'][i]['quote']['USD']['market_cap']
        symbol_1 = data1['data'][i]['symbol']
        id_1 = data1['data'][i]['id']

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
        type_1 = data2['data']["{}".format(id)]['category']

        print ("Coin logo can be found at %s" %(logo))
        print ("Coin website is %s" %(website))
        print ("Coin type is: %s" %(type))

        # data = (name, symbol, logo, website, type)

        # query1 = "INSERT INTO coin(name, symbol, logo, website, cointype) VALUES(%s, %s, %s, %s, %s);"
        # cur.execute(query1, data)


        p = Coins(id=id_1,name=name_1,symbol=symbol_1,url=website,icon=logo,coin_price=price,coin_volume=volume, market_cap=marketcap_1)
        p.save()
        i = i + 1

        print ("Going to sleep for 5 seconds to avoid API throttling")
        print ("      ")
        time.sleep(5)
            # name = models.CharField(max_length=500)
            # symbol = models.TextField()
            # coin_type = models.TextField()
            # url = models.TextField()
            # icon = models.ImageField(upload_to='images/')
            # coin_price = models.DecimalField(max_digits=40, decimal_places=5)
            # coin_volume = models.DecimalField(max_digits=40, decimal_places=5)
            # market_cap = models.DecimalField(max_digits=40, decimal_places=5)


    # conn.commit()
    # cur.close()
    # conn.close()

    
