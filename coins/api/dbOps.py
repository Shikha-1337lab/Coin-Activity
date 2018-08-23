import requests
import json
import time
import coins.models import Coins
# import psycopg2
# dbserver = 'localhost'
# dbname = 'sid'


def readFromDB(coinname):

    conn = psycopg2.connect(host=dbserver,database=dbname) #initialing connection to PostgreSQL DB
    cur = conn.cursor()
    cur.execute("SELECT * from coin WHERE name = '{}'".format(coinname)) #query to get data for a given coinname

    row = cur.fetchone()

    while row is not None: #creating a JSON object from the data returned from DB
        result = {
        "symbol" : row[1],
        "logo" : row[2],
        "website" : row[3],
        "cointype" : row[4]
        }

        row = cur.fetchone() #this shoould be None and should break out of while loop
    return result #send the JSON object back

    conn.commit()
    cur.close()
    conn.close()

def insertDB(): # this is bulk load of data to Database - dont call this function repeatedly
    URL1 = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?sort=market_cap&limit=26&CMC_PRO_API_KEY=d583db45-0e2f-47b3-8038-c639b193aa70"

    r1 = requests.get(url = URL1)
    data1  = r1.json()

    conn = psycopg2.connect(host=dbserver,database=dbname)
    cur = conn.cursor()

    i=0;
    while i<=5:

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

        data = (name, symbol, logo, website, type)

        query1 = "INSERT INTO coin(name, symbol, logo, website, cointype) VALUES(%s, %s, %s, %s, %s);"
        cur.execute(query1, data)

        i = i + 1

        print ("Going to sleep for 5 seconds to avoid API throttling")
        print ("      ")
        time.sleep(5)

    conn.commit()
    cur.close()
    conn.close()




#insertDB()
