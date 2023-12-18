from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
import dashboard.models
from dashboard.views import orders
from .models import Produkt
from .forms import FilterForm, EditItemForm, NewItemForm, NewWydawcaForm, NewTematykaForm


# Create your views here.


def item_list(request):
    if request.method == "POST":
        form = FilterForm(request.POST)
        produkty = Produkt.objects.filter(
            wydawca__nazwa__regex=form.data["wydawca"],
            ilosc__range=[form.data["ilosc_min"], form.data["ilosc_max"]],
            cena__range=[form.data["cena_min"], form.data["cena_max"]],
            wiek__range=[form.data["wiek_min"], form.data["wiek_max"]],
        ).order_by(form.data["sortowanie"])

    else:
        form = FilterForm()
        produkty = Produkt.objects.all()

    return render(request, "item_list.html", {
        "form": form,
        "produkty": produkty
    })


def detail(request, pk):
    produkt = get_object_or_404(Produkt, pk=pk)

    return render(request, "detail.html", {
        "produkt": produkt
    })


@login_required
def delete(request, pk):
    produkt = get_object_or_404(Produkt, pk=pk)
    produkt.delete()

    return redirect("items:item_list")


@login_required
def edit(request, pk):
    produkt = get_object_or_404(Produkt, pk=pk)

    if request.method == "POST":
        form = EditItemForm(request.POST, request.FILES, instance=produkt)

        if form.is_valid():
            form.save()
            return redirect("items:detail", pk=produkt.id)
    else:
        form = EditItemForm(instance=produkt)

    return render(request, "form.html", {
        "form": form,
        "title": "Edycja produktu"
    })


@login_required()
def new_item(requset):
    if requset.method == "POST":
        form = NewItemForm(requset.POST, requset.FILES)

        if form.is_valid():
            produkt = form.save()

        return redirect("items:detail", pk=produkt.id)
    else:
        form = NewItemForm()

    return render(requset, "form.html", {
        "form": form,
        "title": "Utwórz nowy produkt"
    })


@login_required()
def new_wydawca(requset):
    if requset.method == "POST":
        form = NewWydawcaForm(requset.POST)

        if form.is_valid():
            form.save()

        return redirect("items:item_list")
    else:
        form = NewWydawcaForm()

    return render(requset, "form.html", {
        "form": form,
        "title": "Utwórz nowego wydawcę"
    })


@login_required()
def new_tematyka(request):
    if request.method == "POST":
        form = NewTematykaForm(request.POST)

        if form.is_valid():
            form.save()

        return redirect("items:item_list")
    else:
        form = NewTematykaForm()

    return render(request, "form.html", {
        "form": form,
        "title": "Utwórz nową tematykę"
    })


@login_required()
def new_order(request, pk):
    produkt = Produkt.objects.get(pk=pk)
    produkt_ilosc = produkt.ilosc

    if produkt_ilosc > 0:
        produkt_ilosc = produkt_ilosc - 1

        produkt.ilosc = produkt_ilosc
        order = dashboard.models.Zamowienia(produkt=produkt, stan=False, uzytkownik=request.user)

        order.save()
        produkt.save()

    return detail(request, pk)
