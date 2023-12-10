from django.shortcuts import render
from items.models import Produkt
# Create your views here.


def index(request):
    produkty = Produkt.objects.filter(ilosc__range=[1, 3]).order_by('?')[:3]

    return render(request, "core/index.html", {
        "produkty": produkty,
    })
