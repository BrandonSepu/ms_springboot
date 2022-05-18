from django.urls import path 
from . import views

urlpatterns = [
    path("base/", views.base, name="base"),
    path("", views.index, name="index"),
    #login
    path("login/", views.log_in, name="login"),
    path("loginning/", views.loginning, name="loginning"),
    #register
    path("register/", views.register_in, name="register"),
    path("registering/", views.registering, name="registering"),
    #data_info_user
    path("data_user/", views.data_user, name="data_user"),
    path("updateing/", views.updateing, name="updateing"),
    path("deleteing/", views.deleteing, name="deleteing"),
    #data_info_products
    path("productos/", views.productos, name="productos"),
    path("data_products/", views.data_products, name="data_products"),

    path("reg_product/", views.reg_product, name="reg_product"),
    path("registering_pro/", views.registering_pro, name="registering_pro"),
    path("deleteing_pro/", views.deleteing_pro, name="deleteing_pro"),
    path("updateing_pro/", views.updateing_pro, name="updateing_pro"),
    #stock
    path("stock/", views.stock, name="stock"),
    #carrito
    path("tienda", views.tienda, name="tienda")
]
