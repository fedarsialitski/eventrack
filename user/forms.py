from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

from .models import User


class SignupForm(UserCreationForm):
    first_name = forms.CharField(required=False, help_text='Optional')
    last_name = forms.CharField(required=False, help_text='Optional')
    email = forms.EmailField(required=True)

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]

    def signin(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        return user


class SigninForm(AuthenticationForm):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

    class Meta:
        model = User

        fields = [
            'username',
            'password',
        ]

    def signin(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user


class UpdateForm(forms.ModelForm):
    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'first_name',
            'last_name',
            'image_url',
            'thumb_url',
        ]
