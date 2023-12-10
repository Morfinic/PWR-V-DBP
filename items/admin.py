from django.contrib import admin
from .models import Produkt, Wydawca, Tematyka

# Register your models here.

admin.site.register(Produkt)
admin.site.register(Wydawca)
admin.site.register(Tematyka)
