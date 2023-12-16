from django.shortcuts import render
from .models import Produkt
from .forms import FilterForm

# Create your views here.


def item_list(request):
    if request.method == "POST":
        form = FilterForm(request.POST)
        produkty = Produkt.objects.filter(
            wydawca__nazwa__regex=form.data["wydawca"],
            ilosc__range=[form.data["ilosc_min"], form.data["ilosc_max"]],
            cena__range=[form.data["cena_min"], form.data["cena_max"]],
            wiek__range=[form.data["wiek_min"], form.data["wiek_max"]],
        )
        produkty.order_by(form.data["sortowanie"])

    else:
        form = FilterForm()
        produkty = Produkt.objects.all()

    return render(request, "item_list.html", {
        "form": form,
        "produkty": produkty
    })
