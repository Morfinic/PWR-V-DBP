import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Uzytkownik(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    is_admin = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Uzytkownicy"

    def __str__(self):
        return self.username


class Stan(models.Model):
    stan_zamowienia = models.CharField(max_length=30, null=False)

    class Meta:
        verbose_name_plural = "Stany"


    def __str__(self):
        return self.stan_zamowienia


class Zamowienia(models.Model):
    order_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    produkt = models.ForeignKey('items.Produkt', related_name="produkt", on_delete=models.CASCADE)
    stan_zamowienia = models.ForeignKey(Stan, related_name="order_state", on_delete=models.CASCADE)
    uzytkownik = models.ForeignKey(Uzytkownik, related_name="usernames", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Zamówienia"

    def __str__(self):
        return self.order_id
