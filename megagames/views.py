from django.shortcuts import render, get_object_or_404 , redirect   
from django.contrib.auth.decorators import login_required
from .models import Videojuego,Consola,Jugete
from django.contrib.auth import logout
from .forms import VideojuegoForm , ConsolaForm , JugeteForm

# Create your views here.

def index (request):
    context ={}
    return render (request, 'megagames/index.html',context)


def edicion (request):
    context ={}
    return render (request, 'megagames/edicion.html',context)


def juego(request):
    query = request.GET.get('q', '')
    if query:
        videojuegos = Videojuego.objects.filter(nombre__icontains=query)
    else:
        videojuegos = Videojuego.objects.all()
    
    context = {"videojuegos": videojuegos}
    return render(request, 'megagames/juego.html', context)

def detalle_juego(request, nombre):
    videojuego = get_object_or_404(Videojuego, nombre=nombre)  
    context = {"videojuego": videojuego}  
    return render(request, 'megagames/detalle_juego.html', context)

def consolas(request):
    query = request.GET.get('q', '')
    if query:
        consolas = Consola.objects.filter(nombre__icontains=query)
    else:
        consolas = Consola.objects.all()
    
    context = {"consolas": consolas}  
    return render(request, 'megagames/consolas.html', context)


def detalle_consola(request, nombre):
    consola = get_object_or_404(Consola, nombre=nombre)
    context = {"consola": consola}
    return render(request, 'megagames/detalle_consola.html', context)

def jugetes (request):
    query = request.GET.get('q', '')
    if query:
        jugetes = Jugete.objects.filter(nombre__icontains=query)
    else:    
        jugetes = Jugete.objects.all()

    context ={"jugetes":jugetes}
    return render (request, 'megagames/jugetes.html',context)

def detalle_jugete(request, nombre):
    jugete = get_object_or_404(Jugete, nombre=nombre)
    context = {"jugete": jugete}
    return render(request, 'megagames/detalle_jugete.html', context)

def contacto (request):
    context ={}
    return render (request, 'megagames/contacto.html',context)

def perfil (request):
    context ={}
    return render (request, 'megagames/perfil.html',context)

@login_required
def carrito (request):
    context ={}
    return render (request, 'megagames/carrito.html',context)


def juegoraw(request):
    videojuegos = Videojuego.objects.raw('SELECT * FROM megagames_videojuego')
    context = {"videojuegos": videojuegos}
    return render(request, 'megagames/juegoraw.html', context)

def exit(request):
    logout(request)
    return redirect('index')


######## CRUD VIDEOJUEGO 



### Listar juegos 
def lista_videojuegos(request):
    videojuegos = Videojuego.objects.all()
    return render(request, 'megagames/lista_videojuegos.html', {'videojuegos': videojuegos})

def videojuego_crear(request):
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm()
    return render(request, 'megagames/videojuego_crear.html', {'form': form})

def editar_videojuego(request, nombre):
    videojuego = get_object_or_404(Videojuego, nombre=nombre)
    if request.method == 'POST':
        form = VideojuegoForm(request.POST, request.FILES, instance=videojuego)
        if form.is_valid():
            form.save()
            return redirect('lista_videojuegos')
    else:
        form = VideojuegoForm(instance=videojuego)
    return render(request, 'megagames/editar_videojuego.html', {'form': form, 'titulo': f'Editar {videojuego.nombre}'})

def eliminar_videojuego(request, nombre):
    videojuego = get_object_or_404(Videojuego, nombre=nombre)
    if request.method == 'POST':
        videojuego.delete()
        return redirect('lista_videojuegos')
    return render(request, 'megagames/eliminar_videojuego.html', {'videojuego': videojuego})



###### CRUD CONSOLAS 

def lista_consolas(request):
    consolas = Consola.objects.all()
    return render(request, 'megagames/lista_consolas.html', {'consolas': consolas})

def consola_crear(request):
    if request.method == 'POST':
        form = ConsolaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_consolas')
    else:
        form = ConsolaForm()
    return render(request, 'megagames/consola_crear.html', {'form': form})

def editar_consola(request, nombre):
    consola = get_object_or_404(Consola, nombre=nombre)
    if request.method == 'POST':
        form = ConsolaForm(request.POST, request.FILES, instance=consola)
        if form.is_valid():
            form.save()
            return redirect('lista_consolas')
    else:
        form = ConsolaForm(instance=consola)
    return render(request, 'megagames/editar_consola.html', {'form': form, 'titulo': f'Editar {consola.nombre}'})

def eliminar_consola(request, nombre):
    consola = get_object_or_404(Consola, nombre=nombre)
    if request.method == 'POST':
        consola.delete()
        return redirect('lista_consolas')
    return render(request, 'megagames/eliminar_consola.html', {'consola': consola})


#######   CRUD JUGUETES 

def lista_juguetes(request):
    juguetes = Jugete.objects.all()
    return render(request, 'megagames/lista_juguetes.html', {'juguetes': juguetes})

def juguete_crear(request):
    if request.method == 'POST':
        form = JugeteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_juguetes')
    else:
        form = JugeteForm()
    return render(request, 'megagames/juguete_crear.html', {'form': form})

def editar_juguete(request, nombre):
    juguete = get_object_or_404(Jugete, nombre=nombre)
    if request.method == 'POST':
        form = JugeteForm(request.POST, request.FILES, instance=juguete)
        if form.is_valid():
            form.save()
            return redirect('lista_juguetes')
    else:
        form = JugeteForm(instance=juguete)
    return render(request, 'megagames/editar_juguete.html', {'form': form, 'titulo': f'Editar {juguete.nombre}'})

def eliminar_juguete(request, nombre):
    juguete = get_object_or_404(Jugete, nombre=nombre)
    if request.method == 'POST':
        juguete.delete()
        return redirect('lista_juguetes')
    return render(request, 'megagames/eliminar_juguete.html', {'juguete': juguete})