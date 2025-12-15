from django.urls import path  

from . import views


urlpatterns = [
    path('', views.home, name='home'), 
    path('services/', views.services, name='services'),
    path('projets/', views.projets, name='projets'),
    path('equipes/', views.equipes, name='equipes'),
    path('chartes/', views.chartes, name='chartes'),
    path('abouts/', views.abouts, name='abouts'),
    path('contact/', views.contact, name='contact'),
    path('contact/success/', views.contact_success, name='contact_success'),
]