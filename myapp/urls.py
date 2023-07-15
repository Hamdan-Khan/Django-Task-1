from django.urls import path
from .views import *

app_name = "myapp"

urlpatterns = [
    path('', index, name="index"),
    path('details/', details, name="details"),
]
