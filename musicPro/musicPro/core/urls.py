from django.urls import path 
from . import views

urlpatterns = [
    path("base/", views.base, name="base"),
    path("", views.index, name="index"),
    path("productos/", views.productos, name="productos"),
    #login
    path("login/", views.log_in, name="login"),
    path("loginning/", views.loginning, name="loginning"),
    #register
    path("register/", views.register_in, name="register"),
    path("registering/", views.registering, name="registering"),
    #data_info
    path("data_user/", views.data_user, name="data_user"),
]
