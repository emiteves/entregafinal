from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FutbolistaFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dorsal = forms.IntegerField()
    pais = forms.CharField(max_length=50)

class TecnicoFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    pais = forms.CharField(max_length=50)

class SeleccionFormulario(forms.Form):
    pais = forms.CharField(max_length=50)
    grupo = forms.CharField(max_length=1)



class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label = "Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')
        help_texts = {k:"" for k in fields}



class UserEditForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label = "Modificar Nombre")
    last_name = forms.CharField(label = "Modificar Apellido")
    password1 = forms.CharField(label = "Modificar Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label = "Confirmar Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','first_name', 'last_name','password1', 'password2')
        help_texts = {k:"" for k in fields}

