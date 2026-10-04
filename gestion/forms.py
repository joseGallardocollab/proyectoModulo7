from django import forms
from .models import Cliente
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

class RegistroForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'correo@ejemplo.cl'
            }
        ),
        label="Correo electrónico",
        help_text="Ingresa un correo válido para tu cuenta."

    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Usuario'
        })
        self.fields['username'].label = "Nombre de usuario"
        self.fields['username'].help_text = "Debe ser único."

        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
        self.fields['password1'].label = "Contraseña"
        self.fields['password1'].help_text = "Debe tener al menos 8 caracteres."

        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        })
        self.fields['password2'].label = "Confirmar contraseña"
        self.fields['password2'].help_text = "Repite la contraseña para verificar."

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre',
            'email',
            'telefono'
        ]
        widgets = {
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'palceholder': 'Nombre completo',
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control',
                    'palceholder': 'correo@ejemplo.com',
                }
            ),
            'telefono': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'palceholder': '+56 9 1234 5678',
                }
            ),
        }
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class':'form-control aw-input',
                'placeholder':'Usuario',
                'autofocus': True,
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control aw-input',
                'placeholder': 'Contrasena',
            }
        )
    )