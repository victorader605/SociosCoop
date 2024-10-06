from django.db import models

# Create your models here.

class Usuario(models.Model):
    idusuario = models.BigAutoField(primary_key=True)
    nombre_soc = models.CharField(max_length=80, blank=True, null=True)
    apellido_soc = models.CharField(max_length=80, blank=True, null=True)
    rut_soc = models.CharField(max_length=10,blank=True, null=True)
    correo_soc = models.CharField(max_length=80, blank=True, null=True)
    usuario = models.CharField(max_length=30, blank=True, null=True)
    clave = models.CharField(max_length=30, blank=True, null=True)
    idinstitucion = models.IntegerField(null=True)   
    


class Evaluacion(models.Model):
    idevaluacion = models.BigAutoField(primary_key=True)
    rut_eva = models.CharField(max_length=10,blank=True, null=True)
    nombre_eva = models.CharField(max_length=80, blank=True, null=True)
    apellido_eva = models.CharField(max_length=80, blank=True, null=True)
    telefono_eva = models.CharField(max_length=10,blank=True, null=True)
    correo = models.CharField(max_length=80, blank=True, null=True)
    monto_eva = models.IntegerField(null=True)
    plazo_eva = models.IntegerField(null=True)
    idusuario = models.IntegerField(null=True)



class Convenio(models.Model):
    idinstitucion = models.BigAutoField(primary_key=True)
    rut_institucion = models.CharField(max_length=10,blank=True, null=True)
    nombre_isntitucion = models.CharField(max_length=80, blank=True, null=True)