from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings

from .forms import ContactForm


def home_view(request):
    # return HttpResponse('Hello World!')
    return render(request, 'home.html')


def contact_view(request):
    form = ContactForm()
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            
            titre = f'Blog | {nom} {prenom} - {email}'
            send_mail(titre, message, 'settings.EMAIL_HOST_USER', ['testpython207@gmail.com'], fail_silently=False)

        return HttpResponseRedirect(reverse('remerciements'))
    return render(request, 'contact.html', {"form": form})


def remerciements_view(request):
    return HttpResponse("Merci de nous avoir contacté")
