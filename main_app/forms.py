from django import forms
from .models import Pantry, PantryItem, PurchaseLocation, Item


class PantryForm(forms.ModelForm):
  class Meta:
    model = Pantry
    fields = ['name']
    widgets = {
      'name': forms.TextInput
    }

class ItemForm(forms.ModelForm):
  class Meta:
    model = Item
    fields = ['name', 'image', 'purchase_locations']

class PurchaseLocationForm(forms.ModelForm):
  class Meta:
    model = PurchaseLocation
    fields = ['name', 'image']

class PantryItemForm(forms.ModelForm):
  class Meta:
    model = PantryItem
    fields = ['pantry', 'item', 'quantity', 'unit']