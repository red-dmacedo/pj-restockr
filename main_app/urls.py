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
    path('items/new/', views.ItemCreate.as_view(), name='item-create'),
    path('items/<int:pk>/', views.ItemDetail.as_view(), name='item-detail'),
    path('items/<int:pk>/edit/', views.ItemUpdate.as_view(), name='item-update'),
    path('items/<int:pk>/delete', views.ItemDelete.as_view(), name='item-delete'),
    
    path('purchase-locations/', views.PurchaseLocations.as_view(), name='purchase-locations'),
    path('purchase-locations/<int:pk>/', views.PurchaseLocations.as_view(), name='purchase-locations-edit'),
    path('purchase-locations/<int:pk>/delete', views.PurchaseLocationDelete.as_view(), name='purchase-locations-delete'),

    path('pantries/<int:pantry_id>/pantry-item/new/<int:item_id>/', views.PantryItemCreate.as_view(), name="pantryitem-create"),
    path('pantries/<int:pantry_id>/pantry-item/new/', views.PantryItemCreate.as_view(), name="pantryitem-create-new"),
    path('pantry-item/<int:pk>/edit/', views.PantryItemUpdate.as_view(), name="pantryitem-update"),
    path('pantry-item/<int:pk>/delete/', views.PantryItemDelete.as_view(), name="pantryitem-delete"),
]
