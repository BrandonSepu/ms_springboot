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
    #BODEGA
    path("bodega/", views.bodega, name="bodega"),
    path("bodega_aprueba/", views.bodega_aprueba, name="bodega_aprueba"),
    path("reg_product/", views.reg_product, name="reg_product"),
    path("registering_pro/", views.registering_pro, name="registering_pro"),
    path("deleteing_pro/", views.deleteing_pro, name="deleteing_pro"),
    path("updateing_pro/", views.updateing_pro, name="updateing_pro"),
    path("updateing_pro_descuento/", views.updateing_pro_descuento, name="updateing_pro_descuento"),
    #carrito
    path("carrito/", views.carrito , name="carrito"),
    #ventas
    path("venta/", views.venta, name="venta"),
    #redirect
    path("re_admin/", views.re_admin, name="re_admin"),
    #ADMIN
    path("informes/", views.informes, name="informes"),
    #path("agregar_producto<int:id_pro>/", views.agregar_producto, name="agregar_producto"),
    path("agregar_producto1/", views.agregar_producto1, name="agregar_producto1"),
    path("eliminar<int:id_pro>/", views.eliminar_producto, name="del"),
    path("restar_producto/", views.restar_producto, name="restar_producto"),
    path("limpiar/", views.limpiar_carrito, name="CLS"),
    path("save_carrito/", views.save_carrito, name="save_carrito"),
    #VENDEDOR
    path("vendedor/", views.vendedor, name="vendedor"),
    path("vendedor_aprueba/", views.vendedor_aprueba, name="vendedor_aprueba"),
    path("vendedor_rechaza/", views.vendedor_rechaza, name="vendedor_rechaza"),
    #CONTADOR
    path("contador/", views.contador, name="contador"),
    path("contador_aprueba/", views.contador_aprueba, name="contador_aprueba"),
    path("contador_rechaza/", views.contador_rechaza, name="contador_rechaza"),
    #WEBPAY_PLUS

]
'''path("carrito/", views.carrito , name="carrito"),
    '''