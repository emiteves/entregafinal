

from django.urls import path
from entregaTeves import views
from entregaTeves.views import CreacionSeleccion, CreacionTecnico, DetalleSeleccion, DetalleTecnico, EdicionSeleccion, EdicionTecnico, EliminarSeleccion, EliminarTecnico, Error404View, ListaSelecciones, ListaTecnicos, home, futbolistas, futbolistaFormulario, tecnicos, selecciones, buscar, busquedaporPais, tecnicoFormulario, seleccionFormulario, Listafutbolistas, DetalleFutbolista, CreacionFutbolista, EdicionFutbolista, EliminarFutbolista, aboutme, login_request, editarPerfil, register_request, edicion
from django.contrib.auth.views import LogoutView






urlpatterns = [
    path('home/', home, name = 'home'),
    path('', home),
    path('edicion/', edicion, name = 'edicion'),
    path('about/', aboutme, name = 'about'),
    path('futbolistas/', futbolistas, name = 'futbolistas'),
    path('tecnicos/', tecnicos, name = 'tecnicos'),
    path('selecciones/', selecciones, name = 'selecciones'),
    path('futbolistaFormulario/', futbolistaFormulario, name = 'futbolistaFormulario'),
    path('tecnicoFormulario/', tecnicoFormulario, name = 'tecnicoFormulario'),
    path('seleccionFormulario/', seleccionFormulario, name = 'seleccionFormulario'),
    path('buscar/', buscar , name = 'buscar'),
    path('busquedaporPais/', busquedaporPais, name='busquedaporPais'),
    
    
    

##### VIEWS FUTBOLISTAS
    path('futbolistas/list', Listafutbolistas.as_view(), name='lista_futbolistas'),
    path('futbolistas/<pk>', DetalleFutbolista.as_view(), name='futbolista_detalle'),
    path('futbolistas/nuevo/', CreacionFutbolista.as_view(), name='futbolista_crear'),
    path('futbolistas/editar/<pk>', EdicionFutbolista.as_view(), name='futbolista_edicion'),
    path('futbolistas/borrar/<pk>', EliminarFutbolista.as_view(), name='futbolista_borrar'),
##### VIEWS TECNICOS
    path('tecnicos/list', ListaTecnicos.as_view(), name='lista_tecnicos'),
    path('tecnicos/<pk>', DetalleTecnico.as_view(), name='tecnico_detalle'),
    path('tecnicos/nuevo/', CreacionTecnico.as_view(), name='tecnico_crear'),
    path('tecnicos/editar/<pk>', EdicionTecnico.as_view(), name='tecnico_edicion'),
    path('tecnicos/borrar/<pk>', EliminarTecnico.as_view(), name='tecnico_borrar'),
##### VIEWS TECNICOS
    path('selecciones/list', ListaSelecciones.as_view(), name='lista_selecciones'),
    path('selecciones/<pk>', DetalleSeleccion.as_view(), name='seleccion_detalle'),
    path('selecciones/nuevo/', CreacionSeleccion.as_view(), name='seleccion_crear'),
    path('selecciones/editar/<pk>', EdicionSeleccion.as_view(), name='seleccion_edicion'),
    path('selecciones/borrar/<pk>', EliminarSeleccion.as_view(), name='seleccion_borrar'),
# USERS
    path('accounts/login',login_request, name='accounts/login'),
    path('accounts/signup', register_request, name = 'accounts/signup'),
    path('accounts/logout', LogoutView.as_view(template_name='entregaTeves/accounts/logout.html'), name = 'logout'),
    path('accounts/profile', editarPerfil, name = 'accounts/profile'),
    
    

]

