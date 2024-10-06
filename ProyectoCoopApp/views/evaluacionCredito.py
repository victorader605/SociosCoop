
from urllib import response
from django.shortcuts import render
from ProyectoCoopApp.models import EvaluacionCredito
from django.utils import timezone
from django.contrib.auth.models import User
import requests




def evaluacionCredito(request):
    print('Retornar evaluacionCredito.html')
    evaluaciones = EvaluacionCredito.objects.all()
    print("evaluaciones",evaluaciones)
    return render(request, 'evaluacionCredito.html',{'evaluaciones': evaluaciones})

def cargaEvaluacion(request):
    print('evaluacion de credito -> Carga_evaluaciones')
    print('method ->', request.method)
    
    if request.method == 'GET':
        try:
            id_eva = request.GET['id_eva']
            print('codigo ->', id_eva)
            #aqui borra igual que Delete
            evaluacion = evaluacionCredito.objects.get(pk=id_eva)
            evaluacion.delete()
        except Exception as e:
            print(e)
        #contactos = Contacto.objects.all
       # return render(request, 'mantenedor-contacto.html', {'contactos': contactos})
    
    if request.method == 'POST':
        try:
            #lectura de formulario
            id_eva = request.POST['id']
            rut = request.POST['rut']
            estado = 'Respondido'
            resultado = request.POST['resultado']
            observacion = request.POST['observacion']
            f_resolucion = timezone.now()

            # Imprimir los datos
            print('Fecha de resolucion {0}'.format(rut))
            print('Fecha de resolucion {0}'.format(f_resolucion))
            print('Estado de evaluacion {0}'.format(estado))
            print('resultado {0}'.format(resultado))
            print('observacion {0}'.format(observacion))
            
            
            #Busqueda de objeto de la base de datos
            evaluacion = EvaluacionCredito.objects.get(pk=id_eva)
            
            #actualizando en la memoria volatil
            evaluacion.fecha_resolucion_eva = f_resolucion
            evaluacion.estado_eva= estado
            evaluacion.resultado_eva = resultado
            evaluacion.observacion_eva = observacion

            #actualizado en la base de datos
            evaluacion.save(force_update=True)
        except Exception as e:
            print(e)
    evaluaciones = EvaluacionCredito.objects.all() 
    print("evaluaciones",evaluaciones)
    return render(request, 'evaluacionCredito.html', {'evaluaciones': evaluaciones})        


