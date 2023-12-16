from django.shortcuts import render, redirect
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
    if request.user.is_superuser:
        orders = Zamowienia.objects.all()
    else:
        orders = Zamowienia.objects.filter(uzytkownik=request.user.pk)

    return render(request, "zamowienia.html", context={
        "orders": orders
    })
