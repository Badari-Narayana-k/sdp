import pymongo as pymongo
from django.shortcuts import render
from django.http import HttpResponse
import pymongo

client=pymongo.MongoClient('mongodb://localhost:27017')
dbname=client['sdp1']
collection=dbname['flask']
randy={"email":"ksnbnarayan22@gmail.com","type":"astro21"}
collection.insert_one(randy)

def welcome(request):
    umail=request.POST['email']
    passw=request.POST['password']
    finder = {
        "email": umail,
        "password": passw
    }
    flag = 0
    for x in finder:
        if collection.find_one(finder):
            flag = 1
            break

    if flag == 1:
        return render(request,'custo.html')


    else:
        return HttpResponse('<h1 ">wrong id</h1>')
# Create your views here.
#its a request handler
#request -> response

def second(request):
    return render(request, 'second.html')

def index(request):
    return render(request, 'index.html')

def album(request):
    return render(request, 'album.html')

def coverpage(request):
    return render(request, 'coverpage.html')

def custo(request):
    return render(request, 'custo.html')
