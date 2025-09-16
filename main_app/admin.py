from django.contrib import admin
from .models import Pantry, PantryItem, PurchaseLocation, Item


# Register your models here.
admin.site.register(Pantry)
admin.site.register(PantryItem)
admin.site.register(PurchaseLocation)
admin.site.register(Item)
