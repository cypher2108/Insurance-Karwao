from django.contrib import admin

# Register your models here.
from shop.models import Smartphone, Purchase, Claim

admin.site.register(Smartphone)

admin.site.register(Purchase)
admin.site.register(Claim)
