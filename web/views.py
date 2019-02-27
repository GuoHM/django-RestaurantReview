from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.


def list(request):
    context = {
        'text': 'hello'
    }
    return render(request, 'list.html', context)