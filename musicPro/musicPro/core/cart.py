import requests
import json
from django.shortcuts import render, HttpResponse, redirect

from core.apiProducto import getProducto

"""class cart:
    def __init__(self,request):
        self.request = request
        self.session = request.session
        cart = self.session.get("cart")
        if not cart:
            cart = self.session["cart"] = {}
        self.cart = cart

    def add(self, idpro):
        product= getProducto(idpro)
        if str(idpro) not in self.cart.keys():
            self.cart[idpro] = {
                "idpro": idpro,
                "name_pro": product["name_pro"],
                "quantity": 1,
                "pric_pro": product["pric_pro"],
                "des_pro": product["des_pro"]
            }
        else:
            for key, value in self.cart.items():
                if key == str(idpro):
                    value["quantity"] = value ["quantity"] + 1
                    break
        print("parece que funciona")
        self.save()


    def save(self):
        self.session["cart"] = self.cart
        self.session.modified = True

    def remove(self.product):
        product.id =str(product.id)
        if product_id in self.cart:
            del self.cart[product.id]
            self.save()
    
    def decrement(self, product)
        for key, value in self.cart.items():
            if key == str(product.id):
                value["quantity"] = value ["quantity"] - 1
                if value ["quantity"] <1:
                    self.remove(product)
                else:
                    self.save()
                break
    
    def clear(self):
        self.session[]
        self.session.modified = True"""

def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos': productos})

def agregarProducto(request, producto.id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto.id)
    carrito.agregar(producto)
    return redirect("core:tienda")

def eliminarProducto(request, producto_id):
    carrito = Carrito(request)
    productos = Producto.objects.get(id=producto.id)
    carrito.eliminar(producto)
    return redirect("core:tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    productos = Producto.objects.get(id=producto.id)
    carrito.restar(producto)
    return redirect("core:tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("core:tienda")

