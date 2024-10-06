from django.db import models

  
class Usuario(models.Model):
    idusuario_soc = models.BigAutoField(primary_key=True)
    nombre_soc = models.CharField(max_length=80, blank=True, null=True)
    apellido_soc = models.CharField(max_length=80, blank=True, null=True)
    rut_soc = models.CharField(max_length=10,blank=True, null=True)
    correo_soc = models.CharField(max_length=80, blank=True, null=True)
    usuario_soc = models.CharField(max_length=30, blank=True, null=True)
    clave_soc = models.CharField(max_length=30, blank=True, null=True)
    
    
    class Meta:
        managed = True
        db_table = 'Usuario'   
    


class EvaluacionCredito(models.Model):
    id_eva = models.BigAutoField(primary_key=True)
    rut_eva = models.CharField(max_length=10,blank=True, null=True)
    nombre_eva = models.CharField(max_length=80, blank=True, null=True)
    telefono_eva = models.CharField(max_length=10,blank=True, null=True)
    correo_eva = models.CharField(max_length=80, blank=True, null=True)
    monto_eva = models.IntegerField(null=True)
    plazo_eva = models.IntegerField(null=True)
    valorCuota_eva = models.IntegerField(null=True)
    tasa_eva = models.CharField(max_length=10,blank=True, null=True)
    fecha_primer_venc = models.DateField(null=True, blank=True)
    fecha_simulacion_eva = models.DateTimeField(null=True, blank=True)
    fecha_resolucion_eva = models.DateTimeField(null=True, blank=True)
    estado_eva = models.CharField(max_length=30,blank=True, null=True)
    resultado_eva = models.CharField(max_length=30,blank=True, null=True)
    observacion_eva = models.CharField(max_length=500,blank=True, null=True)
   

    class Meta:
        managed = True  # Cambia esto a True
        db_table = 'EvaluacionCredito'




class Convenio(models.Model):
    idinstitucion = models.BigAutoField(primary_key=True)
    rut_institucion = models.CharField(max_length=10,blank=True, null=True)
    nombre_isntitucion = models.CharField(max_length=80, blank=True, null=True)

    class Meta:
        managed = True  # Cambia esto a True
        db_table = 'Convenio'
