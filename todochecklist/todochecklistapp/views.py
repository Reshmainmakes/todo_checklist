from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.urls import reverse_lazy


def add(request):
    return render(request, 'index.html')


def opening(request):
    return render(request, "opening.html")


def restroomcleaning(request):
    return render(request, "restroom_cleaning.html")


def transition(request):
    return render(request, "transition.html")


def closing(request):
    return render(request, "closing.html")
# def home(request ):
#
#     return render(request,"index.html")