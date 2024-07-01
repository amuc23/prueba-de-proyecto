from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistroForm, LoginForm

def registro_view(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redirige a la página de inicio después del registro exitoso
    else:
        form = RegistroForm()
    
    return render(request, 'registro/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Redireccionar a la página de inicio después del login exitoso
                return redirect('megagames:index')  # Asegúrate de que 'megagames:index' sea la URL correcta
    else:
        form = LoginForm()
    
    return render(request, 'registro/login.html', {'form': form})