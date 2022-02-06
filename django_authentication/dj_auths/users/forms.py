from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create a form class called LoginForm which inherits from the built-in autheng.forms.UserCreationForm
class LoginForm(AuthenticationForm):
    remember_me = forms.BooleanField(required=False, initial=False)
    class Meta:
        model = User
        fields = ('username', 'password', 'remember_me')
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'remember_me': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

# This is a class based registration form based on the UserCreationForm
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
                'first_name','last_name','username',
                'email', 'password1', 'password2'
                ]
        widgets = {
            'first_name' : forms.TextInput(attrs={
                'placeholder': 'Enter your first name',
                'class': 'form-control'
            }),
            'last_name' : forms.TextInput(attrs={
                'placeholder': 'Enter your last name',
                'class': 'form-control'
            }),
            'username' : forms.TextInput(attrs={
                'placeholder': 'Enter your username',
                'class': 'form-control'
            }),
            'email' : forms.TextInput(attrs={
                'placeholder': 'Enter your email',
                'class': 'form-control'
            }),
            'password1' : forms.TextInput(attrs={
                'placeholder': 'Enter your password',
                'class': 'form-control',
                'id': 'password'
            }),
            'password2' : forms.TextInput(attrs={
                'placeholder': 'Confirm your password',
                'class': 'form-control',
                'id': 'password'
            }),
        }

