from urllib import response
from django.shortcuts import render
from datetime import datetime
from ProyectoCoopApp.models import EvaluacionCredito
import requests


def credito(request):
    print('Retornar evaluacionCredito.html')
    return render(request, 'simulaCredito.html',)

def formulario_credito(request):
    print('Retornar pagina evaluacionCredito.html')
    
    contexto = {}

    if request.method == 'GET':
        print('Invocación por método GET')
        nombre = request.GET.get('nombre')
        print('nombre {0}'.format(nombre))
        contexto['nombre'] = nombre
        
    elif request.method == 'POST': 
        print('Invocación por método POST')
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        monto = request.POST.get('monto')
        plazo = request.POST.get('plazo')
        fecha = request.POST.get('fecha')
        tasa = '0.029'

        # Convertir los valores de monto y plazo a números para calcular
        try:
            monto = int(monto)
            plazo = int(plazo)
            tasa = float(tasa)
            

            # Calcular valor cuota
            if plazo > 0:
                valor_cuota = int((monto / plazo) * (1 + tasa))
                
            else:
                valor_cuota = 0  # Evitar división por cero

            # Imprimir los datos
            print('rut {0}'.format(rut))
            print('nombre {0}'.format(nombre))
            print('apellido {0}'.format(apellido))
            print('correo {0}'.format(correo))
            print('monto {0}'.format(monto))
            print('plazo {0}'.format(plazo))
            print('valor_cuota {0}'.format(valor_cuota))
            print('fecha {0}'.format(fecha))

            # Pasar las variables al contexto para renderizar
            contexto = {
                'rut': rut,
                'nombre': nombre,
                'apellido': apellido,
                'correo': correo,
                'telefono' : telefono,
                'monto': monto,
                'plazo': plazo,
                'tasa': tasa,
                'valor_cuota': valor_cuota,
                'fecha' : fecha,
            }

        except ValueError:
            print("Error al convertir los valores de monto o plazo")

    return render(request, 'simulaCredito.html', contexto)


def guardar_evaluacion_credito(request):
    print('Guardar evaluacion en la BD')
    
    if request.method == 'GET':
        print('Invocación por método GET')
        nombre = request.GET.get('nombre')
        print('nombre {0}'.format(nombre))
       
        
    elif request.method == 'POST': 
        print('Invocación por método POST')
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        telefono = request.POST.get('telefono')
        monto = request.POST.get('monto')
        plazo = request.POST.get('plazo')
        cuota = request.POST.get('valor_cuota')
        fecha_primer_venc = request.POST.get('fecha')
        tasa = request.POST.get('tasa')
        fecha_simulacion = datetime.today()
        estado = 'Ingresada'

            # Imprimir los datos
        print('rut {0}'.format(rut))
        print('nombre {0}'.format(nombre))
        print('correo {0}'.format(correo))
        print('monto {0}'.format(monto))
        print('plazo {0}'.format(plazo))
        print('valor cuota {0}'.format(cuota))
        print('fecha primer vencimiento {0}'.format(fecha_primer_venc))
        print('fecha simulacion {0}'.format(fecha_simulacion))

        # Convertir la fecha a formato datetime (YYYY-MM-DD)
        try:
            fecha_formateada = datetime.strptime(fecha_primer_venc, '%d/%m/%Y').date()  # Cambia el formato según lo que recibes
        except ValueError:
            # Manejar el error si la fecha no está en el formato correcto
            print('Formato de fecha incorrecto')
            return render(request, 'evaluacionCredito.html', {'error': 'Formato de fecha incorrecto'})
        #Guardar en la Base de datos Socios
            
        credito = EvaluacionCredito()
        credito.rut_eva = rut
        credito.nombre_eva = nombre
        credito.correo_eva = correo
        credito.telefono_eva = telefono
        credito.monto_eva = monto
        credito.plazo_eva = plazo
        credito.valorCuota_eva = cuota
        credito.fecha_primer_venc = fecha_formateada
        credito.tasa_eva = tasa
        credito.fecha_simulacion_eva = fecha_simulacion
        credito.estado_eva = estado
        credito.save()

    return render(request, 'simulaCredito.html')

