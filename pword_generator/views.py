from django.shortcuts import render
from django.http import HttpResponse
import random


# Create your views here.
def home(request):
    return render(request,'pword_generator/home.html')

def password(request):

# first make a list of characters
    characters = list('abcdefghijklmnopqrstuvwxyz')

## then check for Uppercase condition
    if request.GET.get('uppercase'):
        characters.extend(list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

    if request.GET.get('special'):
        characters.extend(list('!£$%^&*+/#<>~\|'))

    if request.GET.get('numbers'):
        characters.extend(list('0123456789'))


    lenght = int(request.GET.get('length',12))

    thepassword = ''

    for x in range(lenght):
        thepassword += random.choice(characters)

    return render(request,'pword_generator/password.html', {'password':thepassword})

def about(request):
    return render(request,'pword_generator/about.html')
