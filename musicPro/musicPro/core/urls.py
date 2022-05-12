from django.urls import path 
from . import views

urlpatterns = [
    path("base/", views.base, name="base"),
    path("", views.index, name="index"),
    path("productos/", views.productos, name="productos"),
]
