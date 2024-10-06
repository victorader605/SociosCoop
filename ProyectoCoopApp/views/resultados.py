import openpyxl
from django.http import HttpResponse
from urllib import response
from django.shortcuts import render
from ProyectoCoopApp.models import EvaluacionCredito
from django.utils import timezone
from django.contrib.auth.models import User

def resultado(request):
    print('Retornar resultado.html')
    evaluaciones = EvaluacionCredito.objects.all()
    print("evaluaciones",evaluaciones)
    return render(request, 'resultado.html',{'evaluaciones': evaluaciones})

def exportar_evaluaciones_excel(request):
    # Crear un libro y hoja de trabajo
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Evaluaciones"

    # Definir los encabezados de las columnas
    columnas = [
        "Código", "Rut", "Nombre", "Monto", "Plazo", "Cuota",
        "Fecha Simulación", "Fecha Resolución", "Estado", "Resultado"
    ]
    ws.append(columnas)

    # Obtener los datos de la base de datos
    evaluaciones = EvaluacionCredito.objects.all()

    # Agregar los datos a la hoja de trabajo
    for evaluacion in evaluaciones:
        ws.append([
            evaluacion.id_eva,
            evaluacion.rut_eva,
            evaluacion.nombre_eva,
            evaluacion.monto_eva,
            evaluacion.plazo_eva,
            evaluacion.valorCuota_eva,
            evaluacion.fecha_simulacion_eva.strftime('%Y-%m-%d %H:%M:%S') if evaluacion.fecha_simulacion_eva else '',
            evaluacion.fecha_resolucion_eva.strftime('%Y-%m-%d %H:%M:%S') if evaluacion.fecha_resolucion_eva else '',
            evaluacion.estado_eva,
            evaluacion.resultado_eva
        ])

    # Crear la respuesta HTTP con el archivo Excel
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response['Content-Disposition'] = 'attachment; filename="evaluaciones_credito.xlsx"'

    # Guardar el archivo Excel en la respuesta
    wb.save(response)
    
    return response