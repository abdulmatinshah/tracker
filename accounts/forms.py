from django import forms
from django.contrib.auth.views import AuthenticationForm
from tracks.models import Track


class PrettyLoginForm(AuthenticationForm):

    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'You username here'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'You username here'}))

    # class Meta:
    #     widgets = {
    #         'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'You username here'})
    #      }

    # def __init__(self, *args, **kwargs):
    #     super(MyLoginForm, self).__init__(*args, **kwargs)
    #     self.fields['username'].widget.placeholder = 'Username'
    #     self.fields['password'].widget.placeholder = 'Password'


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))

