from django import forms
from .models import Wydawca


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
