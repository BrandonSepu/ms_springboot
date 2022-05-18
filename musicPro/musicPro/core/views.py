from django.shortcuts import redirect, render
from core.apiBodega import getAllBodega
from core.apiProducto import delProductoById, getAllPro, getProducto, loadProducto, updateProducto
from core.apiUser import delUserById, getAllUsers, getUserByEmail, loadUser, login, updateUser
from django.contrib import messages

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
            return redirect("index")
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
        tipo_user = "cliente"
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
    

    return render(request, 'web/data_user.html', context)

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
    datalen = len(getAllPro())
    data = getAllPro()
    context = {"data" : data}
    return render(request, 'web/productos.html', context)

def data_products(request):
    dataBodega = getAllBodega()
    datalen = len(getAllPro())
    data = getAllPro()
    
    #for s in dataStock:
    for i in data:
        for s in dataBodega:
            #print("producto: " + i["id_pro"])
            print("bodega: "+ s["producto_id"])
            if (i["id_pro"]) == (s["producto_id"]):
                print("si son iguales")
                print("producto: "+ i["nom_pro"] +" stock: "+ s["stock_bod"])
        
        #if i["id_pro"] == s["producto_id"]:
            #print(i["nom_pro"] + " stock: " + s["stock_bod"])
            #   print("son iguales las id")
        #else:
            #   print("no funciona")
    context = {"data" : data,
                "datalen" : datalen,
                "dataBodega":dataBodega}

    return render(request, 'product/data_products.html', context)

def reg_product(request):
    return render(request, 'product/reg_product.html')

def registering_pro(request):
    try:
        nom_pro = request.POST["nom_pro"]
        tipo = request.POST["tipo_id_tipo"]
        pric_pro = request.POST["pric_pro"]
        des_pro = request.POST["des_pro"]
        
        if tipo == "guitarra cuerpo solido":
            tipo_id_tipo= 1
        elif tipo == "guitarra acustica":
            tipo_id_tipo= 2
        elif tipo == "guitarra electrica":
            tipo_id_tipo= 3
        elif tipo == "bajo 4 cuerda":
            tipo_id_tipo= 4
        elif tipo == "bajo 5 cuerdas":
            tipo_id_tipo= 5
        elif tipo == "bajos activos":
            tipo_id_tipo= 6
        elif tipo == "bajos pasivos":
            tipo_id_tipo= 7
        elif tipo == "piano de media cola":
            tipo_id_tipo= 8
        elif tipo == "piano de cola entera":
            tipo_id_tipo= 9
        elif tipo == "pianolas":
            tipo_id_tipo= 10
        elif tipo == "bateria acustica":
            tipo_id_tipo= 11
        elif tipo == "bateria electrica":
            tipo_id_tipo= 12
        elif tipo == "amplificadores cabezales":
            tipo_id_tipo= 13
        elif tipo == "amplificadores cajas":
            tipo_id_tipo= 14
        else:
            tipo_id_tipo= 15
        
        status = loadProducto(nom_pro,des_pro,pric_pro,tipo_id_tipo)
        if status == True:
            print(status)
            messages.add_message(request=request, level=messages.SUCCESS, message="Registrado con exito : " + nom_pro)
            return redirect("data_products")
        else:
            print(status)
            messages.add_message(request=request, level=messages.ERROR, message="DATOS INCORRECTOS")
            return redirect("register")
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
            tipo_id_tipo= data["tipo_id_tipo"]
            updateProducto(id_pro,nom_pro,des_pro,str(pric_pro),tipo_id_tipo)
            return redirect("data_products")
        else:
            print("error desconocido :C")
    except Exception as e:
        print(e)
    
#LOGICA STOCK

def stock(request):
    dataPro = getAllPro()
    dataStock = getAllBodega()
    context = {"dataPro" : dataPro,
                "dataStock" : dataStock}
    return render(request, 'product/stock.html', context)

#TIENDA
def tienda(request):
    datalen = len(getAllPro())
    data = getAllPro()

    context = {"data" : data}
    return render(request, 'web/tienda.html', context)

    

    
    
