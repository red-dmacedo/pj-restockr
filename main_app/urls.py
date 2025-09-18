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
    path('pantries/<int:pantry_id>/item/<int:pk>', views.PantryBaseItemUpdate.as_view(), name='pantry-base-item-update'),

    path('items/', views.Items.as_view(), name="item-index"),
    path('items/new', views.ItemCreate.as_view(), name='item-create'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('items/<int:pk>/edit/', views.ItemUpdate.as_view(), name='item-update'),
    path('items/<int:pk>/delete', views.ItemDelete.as_view(), name='item-delete'),
]
