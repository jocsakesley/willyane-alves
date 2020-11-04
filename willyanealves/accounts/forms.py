from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    name = forms.CharField(label="Nome", max_length=255)
    last_name = forms.CharField(label="Sobrenome", max_length=255)
    user = forms.SlugField(label="Usuário", max_length=255)
    email = forms.EmailField(label="E-mail")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput(), max_length=255)
    password2 = forms.CharField(label="Repita a senha", widget=forms.PasswordInput(), max_length=255)

class LoginForm(forms.Form):
    user = forms.CharField(label="Usuário", max_length=255)
    password = forms.CharField(label="Senha", max_length=255, widget=forms.PasswordInput())
