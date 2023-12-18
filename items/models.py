from django.db import models
# Create your models here.


class Wydawca(models.Model):
    nazwa = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    adres = models.CharField(max_length=255)

    class Meta:
        ordering = ('nazwa',)
        verbose_name_plural = 'Wydawcy'

    def __str__(self):
        return self.nazwa


class Tematyka(models.Model):
    temat = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Tematyki"


    def __str__(self):
        return self.temat


class Produkt(models.Model):
    nazwa = models.CharField(max_length=255)
    zdjecie = models.ImageField(upload_to="zdj_produktow", blank=True, null=False)
    wydawca = models.ForeignKey(Wydawca, related_name="produkty", on_delete=models.CASCADE)
    ilosc = models.IntegerField()
    cena = models.FloatField()
    wiek = models.IntegerField()
    tematyka = models.ForeignKey(Tematyka, related_name="teamtyka", on_delete=models.CASCADE)
    trudnosc = models.CharField(max_length=255)

    class Meta:
        ordering = ("nazwa",)
        verbose_name_plural = "Produkty"

    def __str__(self):
        return self.nazwa
