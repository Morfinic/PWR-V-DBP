from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, SwitchStatesForm
from .models import Zamowienia, Stan


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
        orders = Zamowienia.objects.all()
    else:
        orders = Zamowienia.objects.filter(uzytkownik=request.user.pk)

    form = SwitchStatesForm()

    return render(request, "zamowienia.html", context={
        "orders": orders,
        "form": form
    })


@login_required
def switch_status(request, pk):
    if request.method == "POST":
        order = get_object_or_404(Zamowienia, pk=pk)

        form_result = SwitchStatesForm(request.POST)
        order.stan_zamowienia = Stan.objects.get(pk=form_result["stan_zamowienia"].value())

        order.save()

    return redirect("dashboard:orders")
