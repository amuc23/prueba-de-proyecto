from django.urls import path

from .views import vista_registro

urlpatterns = [
    
    #muestra la clase como una vista
    path('',vista_registro.as_view(), name="Autenticacion")
    
]
