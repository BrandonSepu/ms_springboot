from django.urls import include, path

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
    #carrito
    path("tienda/", views.tienda, name="tienda"),
    path("carrito/", views.carrito , name="carrito"),
    path("agregar<id_pro>/", views.agregarProducto, name="add"),
    path("eliminar<id_pro>/", views.eliminar_producto, name="del"),
    path("restar<id_pro>/", views.restar_producto, name="sub"),
    path("limpiar/", views.limpiar_carrito, name="CLS"),
]
