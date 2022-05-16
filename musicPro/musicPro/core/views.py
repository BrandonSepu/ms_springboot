from django.shortcuts import redirect, render
from core.apiUser import getAllUsers, loadUser, login
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
    data = getAllUsers()
    #nom_user = data["nom_user"]
    #dictnom_user = dict(nom_user)
    #email_user = data["email_user"]
    #dictemail_user = dict(email_user)
    #id_user = data["id_user"]
    #dictid_user = dict(id_user)
    #age_user = data["age_user"]
    #dictage_user = dict(age_user)
    #pass_user = data["pass_user"]
    #dictpass_user = dict(pass_user)
    #rut_user = data["rut_user"]
    #dictrut_user = dict(rut_user)
    #tipo_user = data["tipo_user"]
    #dicttipo_user = dict(tipo_user)

    print(data[1])

    return render(request, 'web/data_user.html')
    
