from django import forms

from .models import User

class RegisterUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone','name','password']
        widgets = {
            'password' : forms.PasswordInput(),
        }
        