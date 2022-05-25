from distutils.command.upload import upload
from django.db import models

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

    def __str__(self):
        return f'{self.nom_pro} -> {self.pric_pro}'
