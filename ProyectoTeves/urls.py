from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from entregaTeves.views import Error404View, Error500View





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('entregaTeves.urls')),
   
    
  
]

handler404 = Error404View.as_view()
handler500 = Error500View.as_error_view()