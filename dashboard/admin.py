from django.contrib import admin
from .models import Uzytkownik, Zamowienia, Stan

# Register your models here.

admin.site.register(Uzytkownik)
admin.site.register(Zamowienia)
admin.site.register(Stan)
