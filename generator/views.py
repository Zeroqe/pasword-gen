from django.shortcuts import render
from django.http import HttpResponse
import random

def home(request):
    return render(request, 'generator/home.html')



def password(request):

    thepassword = 'testing'

    characters = list('qwertyuiopasdfghjklzxcvbnm')

    if request.GET.get('uppercase'):
        characters.extend('QWERTYUIOPASDFGHJKLZXCVBNM')

    if request.GET.get('specials'):
        characters.extend('!@#$%^&*()_+=~{[}]:;?><,/')

    if request.GET.get('number'):
        characters.extend('1234567890')

    length = int(request.GET.get('length',12))

    thepassword = ''
    for x in range(length):
        thepassword += random.choice(characters)

    return render(request, 'generator/password.html', {'password':thepassword})


def about(request):
    return render(request, 'generator/about.html')