from django import forms
from .models import MembreEquipe, Projet

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=100, 
        widget=forms.TextInput(attrs={'class':"w-full h-12 sm:h-14 px-4 rounded-xl bg-white/5 border border-white/10 text-white placeholder-slate-500 focus:border-primary outline-none"}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class':"w-full h-12 sm:h-14 px-4 rounded-xl bg-white/5 border border-white/10 text-white placeholder-slate-500 focus:border-primary outline-none"}))
    sujet = forms.CharField(max_length=200, 
        widget=forms.TextInput(attrs={'class':"w-full h-12 sm:h-14 px-4 rounded-xl bg-white/5 border border-white/10 text-white placeholder-slate-500 focus:border-primary outline-none"}))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':"w-full h-32 sm:h-40 px-4 py-3 rounded-xl bg-white/5 border border-white/10 text-white placeholder-slate-500 focus:border-primary outline-none", 'rows':5}))


    