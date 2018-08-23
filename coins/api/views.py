# generic views

from rest_framework import generics, mixins
from coins.models  import Coins
from .serializers import CoinSerializer
from django.db.models import Q
import json
import time
import requests
from django.http import HttpResponse
from django.core import serializers





class CoinAPIView(mixins.CreateModelMixin, generics.ListAPIView): # DetailView CreateView FormView
    lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = CoinSerializer
    #queryset                = BlogPost.objects.all()

    def get_queryset(self):
        qs = Coins.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(
                    Q(name__icontains=query)|
                    Q(symbol__icontains=query)
                    ).distinct()
        return qs
    #
    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}



class CoinRudView(generics.RetrieveUpdateDestroyAPIView): # DetailView CreateView FormView
    lookup_field            = 'pk' # slug, id # url(r'?P<pk>\d+')
    serializer_class        = CoinSerializer
    # permission_classes      = [IsOwnerOrReadOnly]
    # queryset                = Coins.objects.all()

    def get_queryset(self):
        return Coins.objects.all()

    def get_serializer_context(self, *args, **kwargs):
        return {"request": self.request}

def api_all(request,limit):

    count=limit
    # setstart=start

    results =  getAll(count, 1)

    return HttpResponse(json.dumps(results), content_type="application/json")

    # return HttpResponse('<h1>This is Trial page, limit is {}.</h1>'.format(limit))
# def api_all(request):
#
#     if 'limit' in request.args:
#         count = int(request.args['limit']) #getting limit from URL argument - example - /api/v1/coin/all?limit=2&start=3
#     else:
#         return "Error: No count provided. Please provide a count"
#
#     if 'start' in request.args:
#         setstart = int(request.args['start']) #getting startOffset from URL argument - example - /api/v1/coin/all?limit=2&start=3
#     else:
#         return "Error: No start provided. Please provide a start"

    # results = getAll(count, setstart) #this is calling the getAll function in coinmarket.py passing the pagination information. The function there is responsibile to get dynamic data from cmk and static data from local DB
    #
    # return jsonify(results)


def insertDB(request): # this is bulk load of data to Database - dont call this function repeatedly
            URL1 = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?sort=market_cap&limit=50 &CMC_PRO_API_KEY=d583db45-0e2f-47b3-8038-c639b193aa70"

            r1 = requests.get(url = URL1)
            data1  = r1.json()
            #
            # conn = psycopg2.connect(host=dbserver,database=dbname)
            # cur = conn.cursor()

            i=0;
            while i<=27:

                name_1 = data1['data'][i]['name']
                price = data1['data'][i]['quote']['USD']['price']
                volume = data1['data'][i]['quote']['USD']['volume_24h']
                marketcap_1 = data1['data'][i]['quote']['USD']['market_cap']
                symbol_1 = data1['data'][i]['symbol']
                id_1 = data1['data'][i]['id']

                print ("----------------------------------------------")
                print (" This is the details for coin: %s" %(name_1))
                print ("Total cap is %s" %(marketcap_1))
                print ("Volume in the last 24hrs is %s" %(volume))
                print ("Price is %s" %(price))
                print ("Symbol is %s" %(symbol_1))
                print("Id is %s" %(id_1))



                URL2 = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/info?id={}&CMC_PRO_API_KEY=d583db45-0e2f-47b3-8038-c639b193aa70".format(id_1)
                r2 = requests.get(url = URL2)
                data2  = r2.json()

                logo = data2['data']["{}".format(id_1)]['logo']
                website = data2['data']["{}".format(id_1)]['urls']['website'][0]
                type_1 = data2['data']["{}".format(id_1)]['category']

                print ("Coin logo can be found at %s" %(logo))
                print ("Coin website is %s" %(website))
                print ("Coin type is: %s" %(type_1))

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

def getAll(countNum, startOffset):
    print("Limit is %s" %countNum)
    print("Start is %s" %startOffset)
    URL1 = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?sort=market_cap&limit={}&start={}&CMC_PRO_API_KEY=d583db45-0e2f-47b3-8038-c639b193aa70".format(countNum,startOffset)
    r1 = requests.get(url = URL1)
    data1  = r1.json()
    i=0;
    results = []

    # print(data1)

    while i<countNum:

        resultfromcmk = {                   #populating datapoints based on data returned by API call made to coinmarketcap
        "name" : data1['data'][i]['name'],
        "price" : data1['data'][i]['quote']['USD']['price'],
        "volume" : data1['data'][i]['quote']['USD']['volume_24h'],
        "percent change 24h" : data1['data'][i]['quote']['USD']['percent_change_24h'],
        "marketcap" : data1['data'][i]['quote']['USD']['market_cap'],
        }
        resultfromdb = readFromDB(data1['data'][i]['name'])  #this is calling the function in dbOps.py to get data from database for the coin using name variable

        z = resultfromcmk.copy()
        z.update(resultfromdb)

        results.append(z) #sending merged result back



        i = i+1

    return results

def readFromDB(coinname):

    # conn = psycopg2.connect(host=dbserver,database=dbname) #initialing connection to PostgreSQL DB
    # cur = conn.cursor()
    # cur.execute("SELECT * from coin WHERE name = '{}'".format(coinname)) #query to get data for a given coinname

    data = serializers.serialize("json", Coins.objects.filter(name=coinname))

    row = json.loads(data)

    if row is not None: #creating a JSON object from the data returned from DB
        result = {
        "symbol" : row[0]['fields']['symbol'],
        "logo" : row[0]['fields']['icon'],
        "website" : row[0]['fields']['url'],
        "cointype" : row[0]['fields']['coin_type']
        }

    else:
        result = {"error": "Coin name does not exist"}

    return (result) #send the JSON object back

    # conn.commit()
    # cur.close()
    # conn.close()
