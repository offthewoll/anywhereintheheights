from django.shortcuts import render
from mealmatcher.forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html', {'form':form})

def guest(request):
    return render(request, 'guest.html', {'form':guestForm})

def host(request):
    return render(request, 'host.html', {'form':host_form})
