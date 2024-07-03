from django.urls import path
from . import views

app_name="carro_Consolas"



urlpatterns = [ 
    
    #se identifica con add_GAME, etc...  para no confundir con otras funciones
    path("add_CONSOLA/<int:consolaid>/", views.agregar_consola, name="add_CONSOLA"),
    path("del_CONSOLA/<int:consolaid>/", views.eliminar_consola, name="del_CONSOLA"),
    path("minus_CONSOLA/<int:consolaid>/", views.restar_consola, name="minus_CONSOLA"),
    path("clean_CONSOLA", views.limpiar_carro_consola, name="clean_CONSOLA"),
    
    
    ##apartado exclusiv carro
    path("add_CONSOLA2/<int:consolaid>/", views.agregar_consola2, name="add_CONSOLA2"),
    path("del_CONSOLA2/<int:consolaid>/", views.eliminar_consola2, name="del_CONSOLA2"),
    path("minus_CONSOLA2/<int:consolaid>/", views.restar_consola2, name="minus_CONSOLA2"),
    
    
]

    

    