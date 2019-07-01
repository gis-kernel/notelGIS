from django import forms
from django.contrib.auth.models import User
from app.models import UserProfileInfo
from captcha.fields import CaptchaField


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    #is_active = forms.BooleanField(default=False)

    class Meta():
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):
    captcha = CaptchaField()

    class Meta():
        model = UserProfileInfo
        fields = ('profile_pic',)
