from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),

    path('pantries/', views.Pantries.as_view(), name="pantry-index"),
    path('pantries/new/', views.PantryCreate.as_view(), name='pantry-create'),
    path('pantries/<int:pk>/', views.PantryDetail.as_view(), name='pantry-detail'),
    path('pantries/<int:pk>/edit', views.PantryUpdate.as_view(), name='pantry-update'),
    path('pantries/<int:pk>/delete', views.PantryDelete.as_view(), name='pantry-delete'),

    path('items/', views.Items.as_view(), name="item-index"),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('pantries/<int:pk>/delete', views.PantryDelete.as_view(), name='item-delete'),
]
