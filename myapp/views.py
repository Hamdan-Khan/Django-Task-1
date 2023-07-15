from django.shortcuts import render


def index(request):
    return render(request, "myapp/index.html")


def details(request):
    return render(request, "myapp/details.html")
