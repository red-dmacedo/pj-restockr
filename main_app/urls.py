from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('accounts/signup/', views.signup, name='signup'),
    path('pantries/', views.Pantries.as_view(), name="pantry-index"),
    path('pantries/new/', views.PantryCreate.as_view(), name='pantry-create'),
    path('pantries/<int:pk>/', views.PantryDetail.as_view(), name='pantry-detail')
]
