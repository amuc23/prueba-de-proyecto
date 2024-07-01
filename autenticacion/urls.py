from django.urls import path
from . import views

urlpatterns = [
 path('registro/', views.registro_view, name='registro'),  # Nombre 'registro' asignado aquí
 path('login/', views.login_view, name='login'),
    # Otras URLs de la app de autenticación
]