from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from .forms import ItemForm, PurchaseLocationForm, PantryItemForm
from .models import Pantry, PantryItem, PurchaseLocation, Item

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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = Item.objects.filter(owner=self.request.user)
        return context


class PantryUpdate(LoginRequiredMixin, UpdateView):
    model = Pantry
    fields = ['name']


class PantryDelete(LoginRequiredMixin, DeleteView):
    model = Pantry
    success_url = '/pantries/'


class Items(LoginRequiredMixin, ListView):
    model = Item

    def get_queryset(self):
        return Item.objects.filter(owner=self.request.user)


class ItemDetail(LoginRequiredMixin, DetailView):
    model = Item
    template_name = 'main_app/item_detail.html'
    context_object_name = "item"


class ItemCreate(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['name', 'image', 'purchase_locations']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['name', 'image', 'purchase_locations']


class ItemDelete(LoginRequiredMixin, DeleteView):
    model = Item
    success_url = '/items/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["next"] = self.request.GET.get("next", "")
        return context


class PantryBaseItemUpdate(LoginRequiredMixin, UpdateView):
    model = Item
    fields = ['name', 'image', 'purchase_locations']
    template_name = 'main_app/item_form.html'


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


class PurchaseLocations(LoginRequiredMixin, ListView):
    model = PurchaseLocation
    template_name = 'main_app/purchase_locations.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # if self.kwargs["pk"]:
        if "pk" in self.kwargs:
            purchaselocation = PurchaseLocation.objects.get(id=self.kwargs["pk"])
            context["purchaselocation_form"] = PurchaseLocationForm(instance=purchaselocation)
        else:
            context["purchaselocation_form"] = PurchaseLocationForm()
        return context

    def post(self, request, *args, **kwargs):
        if "purchaselocation_update" in request.POST or "purchaselocation_create" in request.POST:
            form = PurchaseLocationForm(request.POST)
            if form.is_valid():
                form.save()
            else:
                form = PurchaseLocationForm()
            return redirect('purchase-locations')

class PurchaseLocationDelete(LoginRequiredMixin, DeleteView):
    model = PurchaseLocation
    success_url = '/purchase-locations/'

class PantryItemCreate(LoginRequiredMixin, CreateView):
    model = PantryItem
    fields = ['pantry', 'item', 'quantity', 'unit']

    def get_initial(self):
        initial = super().get_initial()
        if "pantry_id" in self.kwargs:
            initial["pantry"] = Pantry.objects.get(id=self.kwargs["pantry_id"])
        if "item_id" in self.kwargs:
            initial["item"] = Item.objects.get(id=self.kwargs["item_id"])
        return initial

class PantryItemUpdate(LoginRequiredMixin, UpdateView):
    model = PantryItem
    fields = ['quantity', 'unit']

class PantryItemDelete(LoginRequiredMixin, DeleteView):
    model = PantryItem

    def get_success_url(self):
        pantry = self.object.pantry
        if pantry:
            return reverse('pantry-detail', kwargs={'pk': pantry.id})
        else:
            return reverse('pantry-index')