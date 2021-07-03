from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import Job
from .forms import MessageForm
# Create your views here.



from django.core.mail import send_mail

def home(request):
    jobs = Job.objects
    return render(request, 'UtkarshGaur/Home.html', context={'jobs':jobs})

def about(request):
    return render(request, 'UtkarshGaur/About.html' )

def contact(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            recipients = ['uthebest0607@gmail.com']

            if(cc_myself):
                recipients.append(sender)
            send_mail(subject,message,'utgr0607@gmail.com',recipients)
            return HttpResponseRedirect('/thanks')
    else:
        form = MessageForm
    return render(request, 'UtkarshGaur/Contact.html', context= {'form': form} )

def thanks(request):
    return render(request, 'UtkarshGaur/Thanks.html', context = {})