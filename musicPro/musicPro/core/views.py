from django.shortcuts import render
from core.apiUser import login
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

def log_in(request):
    email1 = request["username"]
    print(email1 + " " + pass1)
    pass1 = request["password"]
    #context = login(email1,pass1)
    return render(request, 'web/login.html')
