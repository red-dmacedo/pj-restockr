from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
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


class PantryCreate(LoginRequiredMixin, CreateView):
    model = Pantry
    fields = ['name']
    success_url = '/pantries/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class PantryDetail(LoginRequiredMixin, DetailView):
    model = Pantry
    template_name = 'main_app/pantry_detail.html'
    context_object_name = "pantry"

class PantryUpdate(LoginRequiredMixin, UpdateView):
    model = Pantry
    fields = ['name']



def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('pantry-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)
