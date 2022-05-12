from django.shortcuts import render

# Create your views here.

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
