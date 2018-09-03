from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from coins.models import Coins
import simplejson as json
import requests
import numpy as np
import simplejson
from django.http import HttpResponse


# Old code
# def home(request):
#    return render(request, 'coins/home.html')

def home(request):
    if request.method == 'POST' and 'login' in request.POST:
            user = auth.authenticate(username=request.POST['username'],password=request.POST['password'])
            if user is not None:
                auth.login(request, user)
                name = str(request.user.username)
                return render(request, 'coins/home.html', {'message' : 'Welcome ' + name})
            else:
                return render(request, 'coins/home.html', {'error' : 'Username or Password is incorrect.'} )


    elif request.method == 'POST' and 'create' in request.POST:
            #User has info and wants an account now!
            if request.POST['password1'] == request.POST['password2']:
                try:
                    user = User.objects.get(username=request.POST['username'])
                    return render(request, 'accounts/signup.html', {'error' : 'Username already exists'} )
                except User.DoesNotExist:
                    user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                    auth.login(request,user)
                    return redirect('home')
            else:
                return render(request, 'coins/home.html', {'error' : 'Passswords must match'} )

    else:
            return render(request, 'coins/home.html')

def logout(request):
    request.method == 'POST'
    auth.logout(request)
    return redirect('home')

def newsfeed_editor(request):
    return render(request, 'coins/newsfeed_editor.html')

def market(request):
    response = requests.get("http://coincap.io/coins")
    coins_1 = json.loads(response.text)
    coins = np.array(coins_1)
    print(response)
    print(coins)
    print(len(coins))

    return render(request, 'coins/market.html', {'coins' : coins} )
# Search Functionality
def search(request):
    # if request.method == 'GET': # this will be GET now
    #     query =  request.GET.get('q') # do some research what it does
    #     try:
    #         results = Coins.objects.filter(name__icontains=query) # filter returns a list so you might consider skip except part
    #         # results = []
    #         # for s in status:
    #         #     results.append(s.coin_name)
    #         return render(request,"coins/search.html", {"results":results})
    #     except:
    #         return render(request,"coins/demo.html",{})

    if request.is_ajax():
        q = request.GET.get('term', '')
        try:
            coins = Coins.objects.filter(name__icontains = q )[:20]
            results = []
            for coin in coins:
                coin_json = {}
                coin_json['id'] = coin.id
                coin_json['label'] = coin.name
                coin_json['value'] = coin.name
                results.append(coin_json)
                data = json.dumps(results)
        except:
            data ='fail'
        mimetype = 'application/json'
        return HttpResponse(data,mimetype)
    else:
        return render(request,'coins/demo.html',{})

    # else:
    #     data = 'fail'
    #     mimetype = 'application/json'
    #     return render(request,"coins/search.html", data)
        # except:
        #     data = 'fail'
        #     return render(data,"coins/demo.html")
