from django.shortcuts import render, redirect
from .models import MembreEquipe, Projet
from .forms import ContactForm  
from django.core.mail import send_mail
from django.views.decorators.cache import cache_page



# Create your views here.
@cache_page(60 * 15)  # 15 minutes
def home(request):
    return render(request, 'core/index.html')

@cache_page(60 * 15)  # 15 minutes
def services(request):
    return render(request, 'core/services.html')

@cache_page(60 * 30) 
def projets(request):
    projets = Projet.objects.all()
    context= {
        'projets':projets
    }

    return render(request, 'core/projets.html',context)

@cache_page(60 * 15)  # 15 minutes
def equipes(request):
    membres = MembreEquipe.objects.all()
    context= {
        'team_members':membres
    }
    return render(request, 'core/equipe.html',context)

@cache_page(60 * 15)  # 15 minutes
def chartes(request):
    return render(request, 'core/charte.html')

@cache_page(60 * 15)  # 15 minutes
def abouts(request):
    return render(request, 'core/propos.html')


def contact(request):
    form = ContactForm()

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data["nom"]
            email = form.cleaned_data["email"]
            sujet = form.cleaned_data["sujet"]
            message = form.cleaned_data["message"]

            contenu = f"Nom : {nom}\nEmail : {email}\n\nMessage :\n{message}"

            send_mail(
                subject="Nouveau message depuis le site Zevyron",
                message=contenu,
                from_email=email,
                recipient_list=["tonemail@gmail.com"],
            )

            return redirect('contact_success')
    return render(request, 'core/contact.html',{"form": form})


def contact_success(request):
    return render(request, 'core/contact_success.html')


def custom_404(request, exception):
    return render(request, "core/404.html", status=404)