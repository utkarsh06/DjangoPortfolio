from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.forms import modelformset_factory
from .forms import *
import os

# Create your views here.


def home(request):
    jobs = Job.objects
    return render(request, 'UtkarshGaur/Home.html', context={'jobs':jobs})

def about(request):
    return render(request, 'UtkarshGaur/About.html' )

def contact(request):
    return render(request, 'UtkarshGaur/Contact.html')
