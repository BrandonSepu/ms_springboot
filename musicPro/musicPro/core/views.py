
import base64
from contextlib import ContextDecorator
from django.http import HttpResponse
from django.shortcuts import redirect, render
import json
from core.Carrito import Carrito
from core.apiProducto import delProductoById, getAllPro, getProducto, loadProducto, updateProducto
from core.apiTipoProducto import getAllTipoPro
from core.apiUser import delUserById, getAllUsers, getUserByEmail, loadUser, login, updateUser
from django.contrib import messages
from core.models import Producto

# Create your views here.
#GENERALES
def base(request):
    return render(request, 'web/base.html')

def index(request):
    return render(request, 'web/index.html')

#LOGICA DEL LOGIN

def log_in(request):
    return render(request, 'web/login.html')

def loginning(request):
    try:
        email_user = request.POST["email_user"]
        pass_user = request.POST["password"]
        status = login(email_user,pass_user)
        if status == True:
            print(status)
            messages.add_message(request=request, level=messages.SUCCESS, message="Logueado con exito : " + email_user)
            data = getUserByEmail(email_user)
            print(data["tipo_user"])
            if data["tipo_user"] == "Cliente":
                return redirect("index")
            elif data["tipo_user"] == "Administrador": 
                return redirect("re_admin")
            elif data["tipo_user"] == "Bodeguero": 
                return redirect("bodega")
            elif data["tipo_user"] == "Vendedor": 
                return redirect("re_vende")
            elif data["tipo_user"] == "Contador": 
                return redirect("venta")
        else:
            print("Ocurrio un error: " + str(status))
            messages.add_message(request=request, level=messages.ERROR, message="DATOS INCORRECTOS")
            return redirect("login")
    except Exception as e:
        print(e)
    
#LOGICA DEL REGISTER
def register_in(request):
    return render(request, 'web/register.html')

def registering(request):
    try:
        nom_user = request.POST["nom_user"]
        rut_user = request.POST["rut_user"]
        age_user = request.POST["age_user"]
        tipo_user = "Cliente"
        email_user = request.POST["email_user"]
        pass_user = request.POST["pass_user"]

        status = loadUser(nom_user,rut_user,age_user,tipo_user,email_user,pass_user)
        if status == True:
            print(status)
            messages.add_message(request=request, level=messages.SUCCESS, message="Registrado con exito : " + nom_user)
            return redirect("login")
        else:
            print(status)
            messages.add_message(request=request, level=messages.ERROR, message="DATOS INCORRECTOS")
            return redirect("register")
    except Exception as e:
        print(e)
    
#logica data_user VISTA ADMIN

def data_user(request):
    datalen = len(getAllUsers())
    data = getAllUsers()
    dictnom = []
    dictemail = []
    dictrut = []
    dictage = []
    dicttipo = []
    dictpass = []

    for person in data:
        dictnom.insert(person["id_user"],person["nom_user"])
        dictemail.insert(person["id_user"],person["email_user"])
        dictrut.insert(person["id_user"],person["rut_user"])
        dictage.insert(person["id_user"],person["age_user"])
        dicttipo.insert(person["id_user"],person["tipo_user"])
        dictpass.insert(person["id_user"],person["pass_user"])
    
    context = {
        "data" : data,
        "datalen" : datalen,
        "dictemail" : dictemail,
        "dictrut" : dictrut,
        "dictage" : dictage,
        "dicttipo" : dicttipo,
        "dictpass" : dictpass,
        "dictnom" : dictnom,
    }
    

    return render(request, 'admin/data_user.html', context)

def deleteing(request):
    id_user = request.POST["id_user"]
    print(id_user)
    delUserById(id_user)
    return redirect("data_user")

def updateing(request):
    
    try:
        if request.method == "POST":
            
            tipo = request.POST["tipo_user"]
            email = request.POST["email_user"] 
            #print(email)
            data = getUserByEmail(email)
            id_user = data["id_user"]
            nom_user = data["nom_user"]
            email
            rut_user= data["rut_user"]
            age_user= data["age_user"]
            tipo
            pass_user= data["pass_user"]
            #print(id_user,nom_user, rut_user, age_user, tipo, email, pass_user)
            updateUser(id_user,nom_user, rut_user, age_user, tipo, email, pass_user)
            return redirect("data_user")
        else:
            print("error desconocido :C")
    except Exception as e:
        print(e)

#LOGICA PRODUCT

def productos(request):
    
    data = getAllPro()
    context = {"data" : data}
    return render(request, 'web/productos.html', context)

def data_products(request):
    datalen = len(getAllPro())
    data = getAllPro()
    
    context = {"data" : data,
                "datalen" : datalen,
                }

    return render(request, 'admin/data_products.html', context)

def reg_product(request):
    data = getAllTipoPro()
    context = {"data":data}
    return render(request, 'product/reg_product.html', context)

def bodega(request):

    datalen = len(getAllPro())
    data = getAllPro()
    users = getAllUsers()
    vendedores = []
    for u in users:
        if u["tipo_user"] == "Vendedor":
            vendedores.append(u)
            print(vendedores)
        else:
            print("no es un vendedor")
    
    context = {"data" : data,
                "datalen" : datalen,
                "vendedores" : vendedores
                }

    return render(request, 'bode/bodega.html', context)

def registering_pro(request):
    try:
        nom_pro = request.POST["nom_pro"]
        #print(nom_pro)
        tipoProduct = request.POST["tipo_id_tipo"]
        #print(tipoProduct)
        pric_pro = request.POST["pric_pro"]
        #print(pric_pro)
        des_pro = request.POST["des_pro"]
        #print(des_pro)
        stock_pro = int(request.POST["stock_pro"])
        #print(stock_pro)
        img_pro = request.FILES["img_pro"]
        img_encode = str(base64.b64encode(img_pro.read()))
        img_encode = img_encode[2:-1]
        '''img_pro = {
                    "mime": "image/jpeg",
                    "data": "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gpP+r9Rnyvbv5nAUPwPQhCCbUrkMk+fVFSXqC4tWBGzX/nWF9fBNbc5tDmX23x29L//aAAwDAQACAAMAAAAQ8888888888888s6S8888888888888f6u888888888888kUD888888888888/gd888888888888nM/wDPPPPPPPPPPPM99vPPPPPPPPL82Y7zvPPPPPPPPMdYYBPPPPPPPPPOswz/ANVBHzzzzzzzZL/SiOzWPzzzzzxO3mrY+YUE7zzzzzxlDhJM/wC/N888888894D+TOw288888888vd/OE20V888888888uJxVV1c8888888888/TlVf888888888/8QAIREBAAICAgICAwAAAAAAAAAAAQARITEQMCBBUGFxgaH/2gAIAQMBAT8Q+MSErD3PGBLndig79sH4685toi2lmY2cbFfU1jqyDojlmUAU74vwdOrRNqoAUYjKiJNLFtmCMzDGvNHSbLL/ACWsC5iWvAGbNUBR8/t7AgvEBUgmRPUnuqKmIKCBQaPPOAXLpRHXKkKeiNwE6CO1o6LC36mC4ZgqGaZe3CVkrodIqsgWeyCocPF8nU7gR98EYFRt7EVk9IgsHe71gP/EACIRAQACAgIBBQEBAAAAAAAAAAEAESExMEEQIEBRYXGBof/aAAgBAgEBPxD35ygQb51lZU5lm/YbV74gdNsA2Ew+mUYPFeXix5thgqYR3Zr5mpXl4dwqDoXFKy2AFojvCAGNRVWhM279Znonxo/2UEWty38wAQVUE1NTD9Isj1/XyKKsxDaKwSXZzrEhZO5dp3Fu2fXjd8xalXtglZBnZb/D12sLvbwMNP7MlEaCK2IrJUIStFxm7uEBTHq6Yr8kJTjx4FPrwwi3ujkAUztUQhS8TjAf/8QAKBABAAEEAQMDBQEBAQAAAAAAAREAITFBUWFxgUCRoRCxwdHwMPHh/9oACAEBAAE/EPVoRAAlXVHl8kIo5mnmzd4SBFpmOkUn2BCNi4AWCZ3jfrQERONCQRk6lt0Bfbb8vBAQ9OTRWADhDloTPDNjz0oyvO4BldC47+rTo+OmPkkK8A5OsbD65Cib2upFm1JUMMypnxwcBUkl+42/RS4GAJVcAUtlfeDEbKrN+Y9WdUwrCIAQgLYJmRKTOoVNgegCwcFEu0yc7aQiMYByroNuqmK3JgIYUZycsRafVuFi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"
                            b'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gpP+r9Rnyvbv5nAUPwPQhCCbUrkMk+fVFSXqC4tWBGzX/nWF9fBNbc5tDmX23x29L//aAAwDAQACAAMAAAAQ8888888888888s6S8888888888888f6u888888888888kUD888888888888/gd888888888888nM/wDPPPPPPPPPPPM99vPPPPPPPPL82Y7zvPPPPPPPPMdYYBPPPPPPPPPOswz/ANVBHzzzzzzzZL/SiOzWPzzzzzxO3mrY+YUE7zzzzzxlDhJM/wC/N888888894D+TOw288888888vd/OE20V888888888uJxVV1c8888888888/TlVf888888888/8QAIREBAAICAgICAwAAAAAAAAAAAQARITEQMCBBUGFxgaH/2gAIAQMBAT8Q+MSErD3PGBLndig79sH4685toi2lmY2cbFfU1jqyDojlmUAU74vwdOrRNqoAUYjKiJNLFtmCMzDGvNHSbLL/ACWsC5iWvAGbNUBR8/t7AgvEBUgmRPUnuqKmIKCBQaPPOAXLpRHXKkKeiNwE6CO1o6LC36mC4ZgqGaZe3CVkrodIqsgWeyCocPF8nU7gR98EYFRt7EVk9IgsHe71gP/EACIRAQACAgIBBQEBAAAAAAAAAAEAESExMEEQIEBRYXGBof/aAAgBAgEBPxD35ygQb51lZU5lm/YbV74gdNsA2Ew+mUYPFeXix5thgqYR3Zr5mpXl4dwqDoXFKy2AFojvCAGNRVWhM279Znonxo/2UEWty38wAQVUE1NTD9Isj1/XyKKsxDaKwSXZzrEhZO5dp3Fu2fXjd8xalXtglZBnZb/D12sLvbwMNP7MlEaCK2IrJUIStFxm7uEBTHq6Yr8kJTjx4FPrwwi3ujkAUztUQhS8TjAf/8QAKBABAAEEAQMDBQEBAQAAAAAAAREAITFBUWFxgUCRoRCxwdHwMPHh/9oACAEBAAE/EPVoRAAlXVHl8kIo5mnmzd4SBFpmOkUn2BCNi4AWCZ3jfrQERONCQRk6lt0Bfbb8vBAQ9OTRWADhDloTPDNjz0oyvO4BldC47+rTo+OmPkkK8A5OsbD65Cib2upFm1JUMMypnxwcBUkl+42/RS4GAJVcAUtlfeDEbKrN+Y9WdUwrCIAQgLYJmRKTOoVNgegCwcFEu0yc7aQiMYByroNuqmK3JgIYUZycsRafVuFi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'
                }'''
        
        tipos = getAllTipoPro()
        nom_tipo = False
        for t in tipos:
            if t["nom_tipo"] == tipoProduct:
                tipo = t
                #print(tipo)
                #print("tipo encontrado")
                break
            
        #print(tipo)
        #print(tipoProduct)
        data = {"nom_pro":nom_pro,"des_pro":des_pro,"pric_pro":pric_pro,
        "tipo":tipo,"stock_pro":stock_pro, "img_pro": img_encode}
        #print(data)
        status = loadProducto(nom_pro,des_pro,pric_pro,stock_pro,tipo, img_encode)
        if status == True:
            print(status)
            messages.add_message(request=request, level=messages.SUCCESS, message="Registrado con exito : " + nom_pro)
            return redirect("data_products")
        else:
            print(status)
            messages.add_message(request=request, level=messages.ERROR, message="DATOS INCORRECTOS")
            return redirect("reg_product")
        #print(img_pro + tipoProduct)
        #return HttpResponse("hello#")    
    except Exception as e:
        print(e)
        

def deleteing_pro(request):
    id_pro = request.POST["id_pro"]
    print(id_pro)
    delProductoById(id_pro)
    return redirect("data_products")
    
def updateing_pro(request):
    
    try:
        if request.method == "POST":

            pric_pro = request.POST["pric_pro"]
            id_pro = request.POST["id_pro"] 
            data = getProducto(id_pro)
            nom_pro = data["nom_pro"]
            des_pro = data["des_pro"]
            desc_pro = data["desc_pro"]
            tipo_id_tipo= data["tipo"]
            #print("resultado id_tipo = " + str(tipo_id_tipo))
            stock_pro = data["stock_pro"]
            img_pro = data["img_pro"]
            updateProducto(id_pro,nom_pro,des_pro,str(pric_pro),stock_pro,desc_pro,img_pro,tipo_id_tipo)
            return redirect("data_products")
        else:
            print("error desconocido :C")
    except Exception as e:
        print(e)

def updateing_pro_descuento(request):
    try:
        if request.method == "POST":
            desc_pro = request.POST["desc_pro"]
            id_pro = request.POST["id_pro"] 
            data = getProducto(id_pro)
            nom_pro = data["nom_pro"]
            des_pro = data["des_pro"]
            tipo= data["tipo"]
            stock_pro = data["stock_pro"]
            img_pro = data["img_pro"]
            pric_pro = data["pric_pro"]
            
            updateProducto(id_pro,nom_pro,des_pro,pric_pro,stock_pro,desc_pro,img_pro,tipo)
            return redirect("data_products")
        else:
            print("error desconocido :C")
    except Exception as e:
        print(e)
    
#VENTAS
def venta(request):
    
    datalen = len(getAllPro())
    data = getAllPro()
    
    context = {"data" : data,
                "datalen" : datalen,
                }

    return render(request, 'ventas/venta.html', context)

#REDIRECT
def re_admin(request):
    return render(request, 'redirect/re_admin.html')


#Admin
def informes(request):
    return render(request, 'admin/informes.html')



#TIENDA
  
  #CARRITO

def carrito(request):
    #return HttpResponse("Hola Pythonizando")
    productos = Producto.objects.all()
    return render(request, "web/carrito.html", {'productos':productos})

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("carrito")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("carrito")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("carrito")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("carrito")