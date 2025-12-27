from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter Username',
        'class':'w-full border-none bg-transparent outline-none placeholder:italic focus:outline-none',
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password',
        'class':'w-full border-none bg-transparent outline-none placeholder:italic focus:outline-none',
    }))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1', 'password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Enter Username',
        'class':'w-full border-none bg-transparent outline-none placeholder:italic focus:outline-none',
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'placeholder':'Enter your email',
        'class':'w-full border-none bg-transparent outline-none placeholder:italic focus:outline-none',
    }))

    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Enter your password',
        'class':'w-full border-none bg-transparent outline-none placeholder:italic focus:outline-none',
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm your password',
        'class':'w-full border-none bg-transparent outline-none placeholder:italic focus:outline-none',
    }))