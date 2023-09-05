import unicodedata
from django import forms
from .models import User
from django.contrib.auth.forms import UserChangeForm,AuthenticationForm
from django.contrib.auth import get_user_model

# 회원가입 폼
class UserRegisterForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['phone','username','email','password']
        widgets = {
        'email': forms.EmailInput(attrs={
            'placeholder': '이메일',
            'class' : 'inputform',
            }),
        'password': forms.PasswordInput(attrs={
            'placeholder': '비밀번호',
            'class' : 'inputform',
            }),
        'username': forms.TextInput(attrs={
            'placeholder': '이름',
            'class' : 'inputform',
            }),
        'phone': forms.TextInput(attrs={
            'placeholder': '휴대폰번호',
            'class' : 'inputform',
            }),
    }

# 유저정보 변경 폼
class UserUpdateForm(UserChangeForm):
    password = None
    class Meta:
        model = get_user_model()
        fields = ['email', 'username','phone']
        widgets = {
        'email': forms.EmailInput(attrs={
            'placeholder': '이메일',
            'class' : 'inputform',
            }),
        'username': forms.TextInput(attrs={
            'placeholder': '이름',
            'class' : 'inputform',
            }),
        'phone': forms.TextInput(attrs={
            'placeholder': '휴대폰번호',
            'class' : 'inputform',
            }),
        }

# 로그인 폼
class UsernameField(forms.CharField):
    def to_python(self, value):
        return unicodedata.normalize("NFKC", super().to_python(value))

    def widget_attrs(self, widget):
        return {
            **super().widget_attrs(widget),
            "autocapitalize": "none",
            "autocomplete": "username",
        }

class UserLoginForm(AuthenticationForm):
    username = UsernameField(widget=forms.TextInput(attrs={"autofocus": True,'placeholder':'휴대폰번호'}))
    password = forms.CharField(
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password",'placeholder':'비밀번호'}),
    )