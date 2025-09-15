from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Pantry, PantryItem, PurchaseLocation

# Create your views here.


class Home(LoginView):
    template_name = 'home.html'

class Pantries(LoginRequiredMixin, ListView):
    model = Pantry
    
    def get_queryset(self):
        return Pantry.objects.filter(owner=self.request.user)