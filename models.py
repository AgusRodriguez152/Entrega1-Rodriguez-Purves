from django.db import models

# Create your models here.

class Goleadores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    club=models.CharField(max_length=50)
    goles=models.IntegerField()


class Asistidores(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    club=models.CharField(max_length=50)
    asistencias=models.IntegerField()


class Rojas(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    club=models.CharField(max_length=50)
    rojas=models.IntegerField()


class Amarillas(models.Model):
    nombre=models.CharField(max_length=50)
    apellido=models.CharField(max_length=50)
    club=models.CharField(max_length=50)
    amarilllas=models.IntegerField()    

    


    







