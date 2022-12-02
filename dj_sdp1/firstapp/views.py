import pymongo as pymongo
from django.shortcuts import render
from django.http import HttpResponse
import pymongo

client=pymongo.MongoClient('mongodb://localhost:27017')
dbname = client['SDP']

# Define Collection
collection = dbname['badari']

def welcome(request):
    umail=request.POST['email-id']
    passw=request.POST['password']
    finder = {
        "email-id": umail,
        "password": passw
    }
    flag = 0
    for x in finder:
        if collection.find_one(finder):
            flag = 1
            break

    if flag == 1:
        return render(request,'album.html')


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
def newuser(request):
    return render(request, 'newuser.html')
def route_newuser(request):

    first_name = request.POST['fname']
    last_name = request.POST['lname']
    mobile = request.POST['mobile']
    email_id = request.POST['email-id']
    password = request.POST['password']
    user_data = {
        "first-name": first_name,
        "last-name": last_name,
        "mobile-number": mobile,
        "email-id": email_id,
        "password": password
    }
    collection.insert_one(user_data)

    return render(request, 'index.html')