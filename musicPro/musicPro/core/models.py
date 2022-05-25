from distutils.command.upload import upload
from django.db import models

from core.apiProducto import getAllPro

# Create your models here.
class Producto(models.Model):
    id_pro = models.IntegerField()
    nom_pro = models.CharField(max_length=64)
    des_pro = models.CharField(max_length=300)
    pric_pro = models.CharField(max_length=30)
    stock_pro = models.IntegerField()
    desc_pro = models.IntegerField()
    img_pro =models.ImageField(upload_to="img")
    tipo = models.IntegerField()
    '''def __init__(id_pro,nom_pro,des_pro,pric_pro,stock_pro,desc_pro,img_pro,tipo):
        self.id_pro = id_pro
        self.nom_pro = nom_pro
        self.des_pro = des_pro
        self.pric_pro = pric_pro
        self.stock_pro = stock_pro
        self.desc_pro = desc_pro
        self.img_pro = img_pro
        self.tipo = tipo'''

    def __str__(self):
        return f'{self.nom_pro} -> {self.pric_pro}'

'''def llenado():
    status = False
    data = getAllPro()
    for d in data:
        print(d)
    return status

llenado()'''