from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.template import RequestContext
from core.apiUser import login
from django.contrib import messages
#from .utils import render_to_pdf, sendEmail
#from django.http import HttpResponse
#from .forms import contactForm, paceinteForm, horaMedicaForm
#from .models import paciente, horaMedica, doctor, hora
#import random

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
