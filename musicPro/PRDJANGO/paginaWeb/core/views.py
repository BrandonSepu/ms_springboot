from os import close, read
from django import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context

# Create your views here.
def apiprueba(request):

    apirpuebahtml = open("C:/Users/Equipo-PC/Desktop/PRDJANGO/paginaWeb/core/templates/apirpueba.html");
    template = Template(apirpuebahtml.read());
    apirpuebahtml.close();
    variables = Context();
    documento = template.render(variables)
    return HttpResponse(documento);

def msn(request):
    msn = open("C:/Users/Equipo-PC/Desktop/PRDJANGO/paginaWeb/core/templates/msn.html");
    template = Template(msn.read());
    msn.close();
    variables = Context();
    documento = template.render(variables)
    return HttpResponse(documento);