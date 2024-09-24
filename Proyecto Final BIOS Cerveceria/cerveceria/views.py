from django.shortcuts import render
from cerveceria.models import Cerveza
from cerveceria.forms import ContactoForm
from django.core.mail import EmailMessage
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request,'index.html' )

def somos(request):
    return render(request, 'somos.html')

def buscar(request):
    consulta = ''
    cerveza_por_nombre = []
    cerveza_por_fabricante = []
    
    if "buscar" in request.GET and request.GET['buscar']:
        consulta = request.GET['buscar']
        
        # Primero busca por nombre de cerveza
        cerveza_por_nombre = Cerveza.objects.filter(nombre__icontains=consulta)
        
        # Despues busca por nombre de fabricante
        cerveza_por_fabricante = Cerveza.objects.filter(fabricante__nombre__icontains=consulta)
        
        # Luego combino ambas busquedas
        cerveza = cerveza_por_nombre | cerveza_por_fabricante
    else:
        cerveza = []

    return render(request, 'resultados.html', {'cerveza': cerveza, 'consulta': consulta})   

def contacto(request):
    if request.method == "POST":
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = "Correo desde la Cervecería"
            contenido = formulario.cleaned_data['mensaje'] + '\n\n'
            contenido += 'Comunicarse al mail: ' + formulario.cleaned_data['correo']
            mail = EmailMessage(titulo, contenido, to=['pablosalina25@gmail.com'])
            try:
                mail.send()
                return render(request, 'correo_enviado.html')
            except:
                return render(request, 'correo_no_enviado.html')
    else:
        formulario = ContactoForm()
    
    return render(request, 'contacto.html', {'formulario': formulario})

def usuario_nuevo(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        try:
            formulario.save()
            return render(request, 'usuario_agregado.html')
        except:
            return render(request,'usuario_nuevo.html' , {'formulario': formulario})
    else:
        formulario = UserCreationForm()
        return render(request, 'usuario_nuevo.html' , {'formulario' : formulario})
    

def ingresar(request):
    if not request.user.is_anonymous:
        return HttpResponseRedirect('/privado')
    elif request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            clave = formulario.cleaned_data.get('password')
            acceso = authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render(request, 'no_usuario.html')
            else:
                return render(request, 'ingresar.html', {'formulario': formulario, 'error': 'Credenciales inválidas'})
        else:
            return render(request, 'ingresar.html', {'formulario': formulario, 'error': 'Formulario no válido'})
    else:
        formulario = AuthenticationForm()
        return render(request, 'ingresar.html', {'formulario': formulario})

        

@login_required(login_url='/ingresar')
def privado(request):
    usuario = request.user
    return render(request, 'privado.html',{'usuario' : usuario})

def salir(request):
    if not request.user.is_anonymous:  
        logout(request)
        return HttpResponseRedirect('/ingresar')
    else:
        return HttpResponseRedirect('/ingresar')
    
def error_404(request, exception):
    return render(request, '404.html', {})

def error_500(request):
    return render(request,'500.html',{})