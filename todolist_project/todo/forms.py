from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms.widgets import PasswordInput, TextInput


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'My login is...'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'My password is...'}))



class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'My login will be...'}), label='Username:')
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'My password will be...'}), label='Password:')
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Rewrite your password...'}), label='Confirm Password:')
    error_css_class = "error"