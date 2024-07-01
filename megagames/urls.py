from django.urls import path
from . import views

urlpatterns = [ 
    path('index' , views.index , name="index" ),
    path('edicion' , views.edicion , name="edicion" ),
    path('juego' , views.juego , name="juego" ),
    path('consolas' ,views.consolas , name="consolas" ),
    path('jugetes' ,views.jugetes , name="jugetes" ),
    path('contacto' ,views.contacto , name="contacto" ),
    path('perfil' ,views.perfil , name="perfil" ),
    path('carrito' ,views.carrito , name="carrito" ),
    path('jugete/<str:nombre>/', views.detalle_jugete, name='detalle_jugete'),
    path('juego/<str:nombre>/', views.detalle_juego, name='detalle_juego'),
    path('consola/<str:nombre>/', views.detalle_consola, name='detalle_consola'),
    path('juegoraw' , views.juegoraw , name='juegoraw' ),

    ##### CRUD JUEGOS
    path('lista_videojuegos/', views.lista_videojuegos, name='lista_videojuegos'),
    path('videojuego_crear/', views.videojuego_crear, name='videojuego_crear'),
    path('editar_videojuego/<str:nombre>/', views.editar_videojuego, name='editar_videojuego'),
    path('eliminar_videojuego/<str:nombre>/', views.eliminar_videojuego, name='eliminar_videojuego'),

    ###### CRUD CONSOLAS
    path('lista_consolas/', views.lista_consolas, name='lista_consolas'),
    path('consola_crear/', views.consola_crear, name='consola_crear'),
    path('editar_consola/<str:nombre>/', views.editar_consola, name='editar_consola'),
    path('eliminar_consola/<str:nombre>/', views.eliminar_consola, name='eliminar_consola'),

    ##### CRUD JUGUETES

    path('lista_juguetes/', views.lista_juguetes, name='lista_juguetes'),
    path('juguete_crear/', views.juguete_crear, name='juguete_crear'),
    path('editar_juguete/<str:nombre>/', views.editar_juguete, name='editar_juguete'),
    path('eliminar_juguete/<str:nombre>/', views.eliminar_juguete, name='eliminar_juguete'),
    
    
]

    

    