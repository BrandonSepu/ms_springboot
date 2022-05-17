from multiprocessing import context
from zlib import DEF_BUF_SIZE
from django.http import HttpResponse
from django.shortcuts import redirect, render
from core.apiUser import getAllUsers, getUserByEmail, loadUser, login, updateUser
from django.contrib import messages

# Create your views here.

def base(request):
    return render(request, 'web/base.html')

def index(request):
    return render(request, 'web/index.html')

def productos(request):
    return render(request, 'web/productos.html')

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
    
#logica data_user

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

def delUser(request):
    
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

    
    
    
