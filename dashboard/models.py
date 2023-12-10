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
