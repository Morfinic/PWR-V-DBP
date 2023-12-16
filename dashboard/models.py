import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Uzytkownik(AbstractUser):
    username = models.CharField(max_length=255, unique=True)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Uzytkownicy"

    def __str__(self):
        return self.username


class Zamowienia(models.Model):
    order_id = models.CharField(max_length=100, unique=True, default=uuid.uuid4)
    produkt = models.ForeignKey('items.Produkt', related_name="produkt", on_delete=models.CASCADE)
    stan = models.BooleanField()
    uzytkownik = models.ForeignKey(Uzytkownik, related_name="usernames", on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Zamówienia"

    def __str__(self):
        return self.order_id
