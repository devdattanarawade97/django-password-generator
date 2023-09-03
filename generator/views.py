from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
import random


def home(request):
    return render(request, 'home.html')


def password(request):

    length = int(request.GET.get('length'))
    alphabates = list('abcdefghijklmnopqrstuvwxyz')
    if request.GET.get('uppercase'):
        alphabates.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        alphabates.extend(list('!@#$%^&*()'))

    password = ''
    for y in range(length):

        password = password+random.choice(alphabates)

    return render(request, 'password.html', {'password': password})
