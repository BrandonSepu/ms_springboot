import requests
import json
from django.shortcuts import render, HttpResponse, redirect
from core.apiProducto import getAllPro, getProducto

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

class Carrito:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrito = self.session.get("carrito")
        if not carrito:
            self.session["carrito"] = {}
            self.carrito = self.session["carrito"]
        else:
            self.carrito = carrito

    def agregar(self, producto):
        id = str(producto.id)
        if id not in self.carrito.keys():
            self.carrito[id]={
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "acumulado": producto.precio,
                "cantidad": 1,
            }
        else:
            self.carrito[id]["cantidad"] += 1
            self.carrito[id]["acumulado"] += producto.precio
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito.keys():
            self.carrito[id]["cantidad"] -= 1
            self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0: self.eliminar(producto)
            self.guardar_carrito()

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
