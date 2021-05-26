from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
# Create your views here.


def home(request):
    jobs = Job.objects
    return render(request, 'UtkarshGaur/Home.html', {'jobs':jobs})

def about(request):
    return render(request, 'UtkarshGaur/About.html' )

def contact(request):
    return render(request, 'UtkarshGaur/Contact.html')