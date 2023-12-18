from django import forms
from .models import Wydawca, Produkt, Tematyka


def get_wydawca_list():
    wydawca = Wydawca.objects.values_list("nazwa", flat=True)
    return [[".*", "--------"]] + [[x, x] for x in wydawca]


class FilterForm(forms.Form):
    class Meta:
        fields = ("sortowanie",)

    sortowanie = forms.ChoiceField(choices=(
        ("nazwa", "A-Z"), ("-nazwa", "Z-A"),
        ("wiek", "Wiek, rosnąco"), ("-wiek", "Wiek, malejąco"),
        ("ilosc", "Ilość, rosnąco"), ("-ilosc", "Ilość, malejąco")), widget=forms.Select(attrs={
            "class": "w-full py-2 px-3 my-2 rounded-xl"
        })
    )

    wydawca = forms.ChoiceField(choices=get_wydawca_list(), widget=forms.Select(attrs={
            "class": "w-full py-2 px-3 my-2 rounded-xl"
        }))

    ilosc_min = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "w-1/3 py-2 px-1 my-2 rounded-xl"
    }), initial=0)
    ilosc_max = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "w-1/3 py-2 px-1 my-2 rounded-xl"
    }), initial=500)

    cena_min = forms.FloatField(widget=forms.NumberInput(attrs={
        "class": "w-1/3 py-2 px-1 my-2 rounded-xl"
    }), initial=0)
    cena_max = forms.FloatField(widget=forms.NumberInput(attrs={
        "class": "w-1/3 py-2 px-1 my-2 rounded-xl"
    }), initial=500)

    wiek_min = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "w-1/3 py-2 px-1 my-2 rounded-xl"
    }), initial=0)
    wiek_max = forms.IntegerField(widget=forms.NumberInput(attrs={
        "class": "w-1/3 py-2 px-1 my-2 rounded-xl"
    }), initial=500)


INPUT_CLASSES = "w-full py-4 px-6 rounded-xl border"


class EditItemForm(forms.ModelForm):
    class Meta:
        model = Produkt
        fields = ("nazwa", "zdjecie", "wydawca", "ilosc", "cena", "wiek", "tematyka", "trudnosc")

        widgets = {
            "nazwa": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            }),
            "zdjecie": forms.FileInput(attrs={
                "class": INPUT_CLASSES,
                # "required": True
            }),
            "wydawca": forms.RadioSelect(attrs={
                "class": "rounded-xl border"
            }),
            "ilosc": forms.NumberInput(attrs={
                "class": INPUT_CLASSES
            }),
            "cena": forms.NumberInput(attrs={
                "class": INPUT_CLASSES
            }),
            "wiek": forms.NumberInput(attrs={
                "class": INPUT_CLASSES
            }),
            "tematyka": forms.RadioSelect(attrs={
                "class": "rounded-xl border"
            }),
            "trudnosc": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            })
        }


class NewItemForm(forms.ModelForm):
    class Meta:
        model = Produkt
        fields = ("nazwa", "zdjecie", "wydawca", "ilosc", "cena", "wiek", "tematyka", "trudnosc")

        widgets = {
            "nazwa": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            }),
            "zdjecie": forms.FileInput(attrs={
                "class": INPUT_CLASSES,
                "required": True
            }),
            "wydawca": forms.RadioSelect(attrs={
                "class": "rounded-xl border"
            }),
            "ilosc": forms.NumberInput(attrs={
                "class": INPUT_CLASSES
            }),
            "cena": forms.NumberInput(attrs={
                "class": INPUT_CLASSES
            }),
            "wiek": forms.NumberInput(attrs={
                "class": INPUT_CLASSES
            }),
            "tematyka": forms.RadioSelect(attrs={
                "class": "rounded-xl border"
            }),
            "trudnosc": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            })
        }


class NewWydawcaForm(forms.ModelForm):
    class Meta:
        model = Wydawca
        fields = ("nazwa", "mail", "adres")

        widgets = {
            "nazwa": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            }),
            "mail": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            }),
            "adres": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            }),
        }


class NewTematykaForm(forms.ModelForm):
    class Meta:
        model = Tematyka
        fields = ("temat",)

        widgets = {
            "temat": forms.TextInput(attrs={
                "class": INPUT_CLASSES
            })
        }