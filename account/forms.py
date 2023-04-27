from django.contrib.auth.forms import AuthenticationForm
from django import forms

from main.models import Account



class CustomAuthenticationForm(AuthenticationForm):
    pass


class EditProfileForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = ['fullname', 'bio', 'profile_image', 'header_image']


