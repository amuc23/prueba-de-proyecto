from django.urls import path
from . import views

app_name="carro_Videojuegos"



urlpatterns = [ 
    
    #se identifica con add_GAME, etc...  para no confundir con otras funciones
    path("add_GAME/<int:videojuego_id>/", views.agregar_videojuego, name="add_GAME"),
    path("del_GAME/<int:videojuego_id>/", views.eliminar_videojuego, name="del_GAME"),
    path("minus_GAME/<int:videojuego_id>/", views.restar_videojuego, name="minus_GAME"),
    path("clean_GAME", views.limpiar_carro_videojuegos, name="clean_GAME"),
    
    
    ##apartado exclusiv carro
    path('add_GAME2/<int:videojuego_id>/', views.agregar_videojuego2, name='add_GAME2'),
    path('del_GAME2/<int:videojuego_id>/', views.eliminar_videojuego2, name='del_GAME2'),
    path('minus_GAME2/<int:videojuego_id>/', views.restar_videojuego2, name='minus_GAME2'),
    
    
]

    

    