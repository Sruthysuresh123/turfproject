from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import User
from app1.models import Booking
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def signup(request):
    return render(request,'signup.html')

def login(request):
    return render(request,'login.html')

def games(request):
    return render(request,'games.html')

def location(request):
    return render(request,'location.html')

def register(request):
    a = request.POST['name']
    c = request.POST['place']
    d = request.POST['phone']
    e = request.POST['email']
    f = request.POST['uname']
    g = request.POST['pass']
    h = User(Name=a,Place=c,Phone=d,Email=e,Username=f,Password=g)
    h.save()
    # return HttpResponse('User Registered Successfully')
    return render(request,'registerhttp.html')

def loged(request):
    try:
        a = User.objects.get(Username=request.POST['username'])
        if a.Password==request.POST['password']:
            return render(request,'loged.html',{'key':a.Username,'key2':a.Name,'key4':a.Place,'key5':a.Phone,'key6':
                                                 a.Email})
        else:
            return HttpResponse('Invalid password')
    except:
        return HttpResponse('Invalid User')


    
  
# def logout_view(request):
#     logout(request)
#     return redirect('home')

# @login_required(login_url='/login')
# def logout_view(request):
#     logout(request)
#     return redirect('login')




def booking(request):
    return render(request,'booking.html')  

def booked(request):
    a = request.POST['name1']
    c = request.POST['place1']
    d = request.POST['phone1']
    e = request.POST['game1']
    f = request.POST['date1']
    h = Booking(Name=a,Place=c,Phone=d,Game=e,Date_Time=f)
    h.save()
    # return HttpResponse('Successfully Booked') 
    return render(request,'bookedhttp.html')
    