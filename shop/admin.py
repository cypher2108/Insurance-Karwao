from django.contrib import admin

# Register your models here.
from shop.models import *

admin.site.register(Smartphone)
admin.site.register(Purchase)
admin.site.register(Claim)
admin.site.register(Laptop)
admin.site.register(Automobile)
admin.site.register(PurchaseLaptop)
admin.site.register(PurchaseAutomobile)
admin.site.register(ClaimLaptop)
admin.site.register(ClaimAutomobile)
