from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm
from .models import Zamowienia

# Create your views here.


def signup(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("dashboard:login")
    else:
        form = SignUpForm()

    return render(request, "signup.html", {
        "form": form
    })


def logout(request):
    logout(request)


def orders(request):
    if request.user.is_admin:
        orders = Zamowienia.objects.all().order_by("stan")
    else:
        orders = Zamowienia.objects.filter(uzytkownik=request.user.pk).order_by("-stan")

    return render(request, "zamowienia.html", context={
        "orders": orders
    })

@login_required
def switch_status(request, pk):
    produkt = get_object_or_404(Zamowienia, pk=pk)
    produkt.stan = not produkt.stan
    produkt.save()

    return redirect("dashboard:orders")
