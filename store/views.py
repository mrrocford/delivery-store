from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
# Create your views here.

def index(request):
    return render(request, "store/index.html")


def shoping_cart(request):
    return render(request, "store/shoping_cart.html")