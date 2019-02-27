from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
# Create your views here.


def list(request):
    restaurants = Restaurant.objects.all();
    return render(request, 'list.html', {'restaurantlist':restaurants})


def login_page(request):
    return render(request, 'login.html')


def login_action(request):
    user = User.objects.get(user_name=request.POST['username'])
    if user.password == request.POST['password']:
        request.session['userid'] = user.user_id
        return render(request, 'list.html',{'text':'success'})
    else:
        return render(request, 'login.html', {'message': 'Invalid login attempt!'})


def logout(request):
    del request.session['userid']
    return render(request, 'login.html')


def detail(request, name):
    restaurants = Restaurant.objects.get(name=name);
    return render(request, 'detail.html', {'name': name})
