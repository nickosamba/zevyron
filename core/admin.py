from django.contrib import admin
from .models import MembreEquipe, Projet


@admin.register(MembreEquipe)
class MembreEquipeAdmin(admin.ModelAdmin):
    list_display = ('nom', 'poste', 'email')
    search_fields = ('nom', 'poste', 'email')
    list_filter = ('poste',)
    ordering = ('nom',)
    fieldsets = (
        (None, {
            'fields': ('nom', 'poste', 'description', 'photo', 'linkedin', 'github', 'email')
        }),
    )


@admin.register(Projet)
class ProjetAdmin(admin.ModelAdmin):
    list_display = ('titre', 'categorie', 'lien_demo', 'lien_github')
    search_fields = ('titre', 'categorie')
    list_filter = ('categorie',)
    ordering = ('titre',)
    fieldsets = (
        (None, {
            'fields': ('titre', 'sous_titre', 'description', 'categorie', 'image', 'lien_demo', 'lien_github')
        }),
    )
