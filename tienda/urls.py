from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('megagames/', include('megagames.urls')),
    
    path('carro_Videojuegos/', include('carro_Videojuegos.urls')),


    path('', RedirectView.as_view(url='/megagames/index', permanent=True)),  # Redirección desde la raíz



    ######################################
    path('autenticacion/', include('autenticacion.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # URLs de autenticación de Django contrib

    
   

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
