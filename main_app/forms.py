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
    fields = ['name']
