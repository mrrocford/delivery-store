from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("shoping_cart", views.shoping_cart, name="shoping_cart")
]