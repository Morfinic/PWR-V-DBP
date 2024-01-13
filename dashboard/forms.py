from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Uzytkownik, Zamowienia


class SignUpForm(UserCreationForm):
    class Meta:
        model = Uzytkownik
        fields = ("username", "email", "password1", "password2")

    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Nazwa użytkownika",
        "class": "w-full py-4 px-6 rounded-xl"
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        "placeholder": "Adres email",
        "class": "w-full py-4 px-6 rounded-xl",
        # "requiered": True
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Hasło",
        "class": "w-full py-4 px-6 rounded-xl"
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Powtórz hasło",
        "class": "w-full py-4 px-6 rounded-xl"
    }))


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        "placeholder": "Nazwa użytkownika",
        "class": "w-full py-4 px-6 rounded-xl"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "placeholder": "Hasło",
        "class": "w-full py-4 px-6 rounded-xl"
    }))


class SwitchStatesForm(forms.ModelForm):
    class Meta:
        model = Zamowienia
        fields = ("stan_zamowienia",)

        widgets = {
            "stan": forms.RadioSelect(attrs={
                "class": "rounded-xl border"
            }
        )}
