from django.urls import path 
from . import views

#rutas
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),
    path('contacto/', views.contacto, name='contacto')
]

