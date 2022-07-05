from audioop import reverse
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from entregaTeves.models import Futbolistas, Selecciones, Tecnicos
from entregaTeves.forms import FutbolistaFormulario, TecnicoFormulario, SeleccionFormulario, UserRegistrationForm, UserEditForm
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


def futbolistas(request):
    futbolistas = Futbolistas.objects.all().order_by('pais')
    contexto = {"Futbolistas":futbolistas}
    return render(request, 'entregaTeves/futbolistas.html', contexto)

def selecciones(request):
    selecciones = Selecciones.objects.all().order_by('grupo')
    contexto = {"Selecciones":selecciones}
    return render(request, 'entregaTeves/selecciones.html', contexto)

def tecnicos(request):
    tecnicos = Tecnicos.objects.all().order_by('pais')
    contexto = {"Tecnicos":tecnicos}
    return render(request, 'entregaTeves/tecnicos.html', contexto)


def home(request): 
    return render(request, 'entregaTeves/home.html')

def edicion(request): 
    return render(request, 'entregaTeves/edicion.html')

def aboutme(request):
    return render(request, 'entregaTeves/about.html')

# Formularios insertar informacion base de datos
@login_required
def futbolistaFormulario (request):
    if request.method == 'POST':
        miFormulario = FutbolistaFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion ['nombre']
            apellido = informacion ['apellido']
            dorsal = informacion ['dorsal']
            pais = informacion ['pais']
            futbolista = Futbolistas (nombre =nombre, apellido =apellido, dorsal =dorsal, pais = pais)
            futbolista.save()
        return render(request, 'entregaTeves/home.html')
    else:
        miFormulario = FutbolistaFormulario()
    return render (request, 'entregaTeves/futbolistaFormulario.html', {'miFormulario':miFormulario})

@login_required
def tecnicoFormulario (request):
    if request.method == 'POST':
        miFormulario = TecnicoFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            nombre = informacion ['nombre']
            apellido = informacion ['apellido']
            pais = informacion ['pais']
            tecnico = Tecnicos (nombre =nombre, apellido =apellido, pais = pais)
            tecnico.save()
        return render(request, 'entregaTeves/home.html')
    else:
        miFormulario = TecnicoFormulario()
    return render (request, 'entregaTeves/tecnicoFormulario.html', {'miFormulario':miFormulario})

@login_required
def seleccionFormulario (request):
    if request.method == 'POST':
        miFormulario = SeleccionFormulario(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            grupo = informacion ['grupo']
            pais = informacion ['pais']
            seleccion = Selecciones (grupo =grupo, pais = pais)
            seleccion.save()
        return render(request, 'entregaTeves/home.html')
    else:
        miFormulario = SeleccionFormulario()
    return render (request, 'entregaTeves/seleccionFormulario.html', {'miFormulario':miFormulario})

###### Busqueda por pais

def busquedaporPais(request):
    return render(request, 'entregaTeves/busquedaporPais.html')

def buscar(request):

    if request.GET['pais']:
        pais = request.GET['pais']
        futbolistas = Futbolistas.objects.filter(pais = pais).order_by('dorsal')
        tecnicos = Tecnicos.objects.filter(pais = pais)
        selecciones = Selecciones.objects.filter(pais = pais)
        return render(request, 'entregaTeves/resultadoBusquedaporPais.html', {'futbolistas':futbolistas, 'pais' : pais, 'tecnicos': tecnicos, 'selecciones':selecciones})
    else:
        respuesta = "Ingrese datos correctamente"
    return HttpResponse(respuesta)

# LISTVIEW

class Listafutbolistas(LoginRequiredMixin,ListView):
    model = Futbolistas
    template_name = 'entregaTeves/lista_futbolistas.html'
  

# VIEWS FUTBOLISTAS 
class DetalleFutbolista(LoginRequiredMixin,DetailView):
  model = Futbolistas
  template_name = 'entregaTeves/futbolista_detalle.html'


class CreacionFutbolista(LoginRequiredMixin,CreateView):
  model = Futbolistas
  success_url = reverse_lazy('lista_futbolistas')
  fields = ['nombre','apellido','dorsal','pais']


class EdicionFutbolista(LoginRequiredMixin,UpdateView):
  model = Futbolistas
  success_url = reverse_lazy('lista_futbolistas')
  fields = ['nombre','apellido','dorsal','pais']


class EliminarFutbolista(LoginRequiredMixin,DeleteView):
  model = Futbolistas
  success_url = reverse_lazy('lista_futbolistas')

#404

class Error404View(TemplateView):
  template_name = "entregaTeves/404.html"

class Error500View(TemplateView):
    template_name = "entregaTeves/500.html"

    @classmethod
    def as_error_view(cls):

        v = cls.as_view()
        def view(request):
            r = v(request)
            r.render()
            return r
        return view


# VIEWS TECNICOS 

class ListaTecnicos(ListView):
    model = Tecnicos
    template_name = 'entregaTeves/lista_tecnicos.html'
    

class DetalleTecnico(LoginRequiredMixin,DetailView):
  model = Tecnicos
  template_name = 'entregaTeves/tecnico_detalle.html'


class CreacionTecnico(LoginRequiredMixin,CreateView):
  model = Tecnicos
  success_url = reverse_lazy('lista_tecnicos')
  fields = ['nombre','apellido','pais']


class EdicionTecnico(LoginRequiredMixin,UpdateView):
  model = Tecnicos
  success_url = reverse_lazy('lista_tecnicos')
  fields = ['nombre','apellido','pais']


class EliminarTecnico(LoginRequiredMixin,DeleteView):
  model = Tecnicos
  success_url = reverse_lazy('lista_tecnicos')

# VIEWS SELECCIONES 

class ListaSelecciones(ListView):
    model = Selecciones
    template_name = 'entregaTeves/lista_selecciones.html'


class DetalleSeleccion(LoginRequiredMixin,DetailView):
  model = Selecciones
  template_name = 'entregaTeves/seleccion_detalle.html'


class CreacionSeleccion(LoginRequiredMixin,CreateView):
  model = Selecciones
  success_url = reverse_lazy('lista_selecciones')
  fields = ['grupo','pais']


class EdicionSeleccion(LoginRequiredMixin,UpdateView):
  model = Selecciones
  success_url = reverse_lazy('lista_selecciones')
  fields = ['grupo','pais']


class EliminarSeleccion(LoginRequiredMixin,DeleteView):
  model = Selecciones
  success_url = reverse_lazy('lista_selecciones')

#logiiiinn 

def login_request(request):
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            clave = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login (request, user) 
                return render(request, 'entregaTeves/home.html', {'mensaje': f'Bienvenido {usuario}'})
        
        else: 
            return render(request, 'entregaTeves/home.html', {'mensaje': 'Hubo un error en tu informacion, intenta nuevamente'})
    else:  
        form = AuthenticationForm()
        return render(request, 'entregaTeves/accounts/login.html', {'form':form})

# registroooo

def register_request(request):
    if request.method =='POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data ['username']
            form.save()
            return render(request, 'entregaTeves/home.html', {'mensaje': f'Usuario {username} creado'})
        else:
            return render(request, 'entregaTeves/home.html', {'mensaje': 'Hubo un error en tu solicitud, intenta nuevamente'})
    else:
        form = UserRegistrationForm()
        return render(request, 'entregaTeves/accounts/signup.html', {'form':form})         


def editarPerfil(request):
    usuario = request.user

    if request.method == 'POST':
        formulario =  UserEditForm(request.POST, instance=usuario)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            usuario.email = informacion ['email']
            usuario.password1 = informacion ['password1']
            usuario.password2 = informacion ['password2']
            usuario.save()
            return render(request, 'entregaTeves/home.html',{'usuario': usuario, 'mensaje':'Datos editados correctamente'})
    
    else:
        formulario = UserEditForm(instance=usuario)
    return render (request, 'entregaTeves/accounts/profile.html', {'formulario':formulario, 'usuario':usuario.username})


