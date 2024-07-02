from django.urls import path
from ..carro_Consolas import views

app_name="carro_Jugetes"



urlpatterns = [ 
    
    #se identifica con add_GAME, etc...  para no confundir con otras funciones
    path("add_GAMEJGT/<int:jugeteid>/", views.agregar_jugete, name="add_GAMEJGT"),
    path("del_GAMEJGT/<int:jugeteid>/", views.eliminar_jugete, name="del_GAMEJGT"),
    path("minus_GAMEJGT/<int:jugeteid>/", views.restar_jugete, name="minus_GAMEJGT"),
    path("clean_GAMEJGT", views.limpiar_carro_jugetes, name="clean_GAMEJGT"),
    
    
    ##apartado exclusiv carro
    path('add_GAMEJGT2/<int:jugeteid>/', views.agregar_jugete2, name='add_GAMEJGT2'),
    path('del_GAMEJGT2/<int:jugeteid>/', views.eliminar_jugete2, name='del_GAMEJGT2'),
    path('minus_GAMEJGT2/<int:jugeteid>/', views.restar_jugete2, name='minus_GAMEJGT2'),
    
    
]

    

    