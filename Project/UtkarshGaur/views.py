from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request, 'UtkarshGaur/Home.html')

def about(request):
    return render(request, 'UtkarshGaur/About.html' )

def contact(request):
    return render(request, 'UtkarshGaur/Contact.html')