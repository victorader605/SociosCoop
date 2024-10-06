import plotly.express as px
import json
from django.shortcuts import render
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from datetime import datetime
from ProyectoCoopApp.models import EvaluacionCredito
from plotly.utils import PlotlyJSONEncoder  # Importar la clase correcta
import calendar


   

def generar_grafico_barra(request):
    year = datetime.now().year

    # Obtener los datos de evaluaciones agrupados por mes
    datos = (EvaluacionCredito.objects
             .filter(fecha_resolucion_eva__year=year)  # Cambia 'fecha_resolucion_eva' por el campo correcto
             .annotate(mes=TruncMonth('fecha_resolucion_eva'))  # Asegúrate de que 'fecha_resolucion_eva' sea el campo correcto
             .values('mes')
             .annotate(total_monto=Sum('monto_eva'))  # Cambia 'monto_eva' por el campo correcto
             .order_by('mes'))

    # Crear un diccionario con todos los meses del año y valores por defecto en 0
    meses_dict = {month: 0 for month in range(1, 13)}

    # Llenar el diccionario con los datos obtenidos de la base de datos
    for dato in datos:
        meses_dict[dato['mes'].month] = dato['total_monto']

    # Extraer los nombres de los meses en español y los valores correspondientes
    meses = [calendar.month_name[mes].capitalize() for mes in meses_dict.keys()]
    total_montos = list(meses_dict.values())

    # Crear el gráfico de barras con Plotly (solo montos)
    fig = px.bar(
        x=meses,
        y=total_montos,
        labels={'x': 'Mes', 'y': 'Total Monto'},
       
    )

    # Cambiar el título y etiquetas al español
    fig.update_layout(
        
        xaxis_title='Mes',
        yaxis_title='Monto Total'
    )

    # Convertir el gráfico a JSON para pasarlo a la plantilla
    graph_json_barra = json.dumps(fig, cls=PlotlyJSONEncoder)
    print('Retornar grafico barra')

    # Renderizar la plantilla y pasar el gráfico
    return graph_json_barra

def generar_grafico_circular(request):
    # Obtener la cantidad de evaluaciones aprobadas y rechazadas
    datos = (
        EvaluacionCredito.objects
        .values('resultado_eva')  # Asegúrate de que 'resultado_eva' sea el campo que indica el estado
        .annotate(cantidad=Count('id_eva'))
    )

    # Extraer los resultados y cantidades para el gráfico
    resultados = [dato['resultado_eva'] for dato in datos]
    cantidades = [dato['cantidad'] for dato in datos]

    # Crear el gráfico circular con Plotly
    fig = px.pie(
        names=resultados,
        values=cantidades,
        color_discrete_sequence= ['green', 'red']#px.colors.sequential.RdBu  # Puedes personalizar los colores aquí
    )

    # Convertir el gráfico a JSON para pasarlo a la plantilla
    graph_json_circular = json.dumps(fig, cls=PlotlyJSONEncoder)
    print('Retornar grafico circula')

    # Renderizar la plantilla y pasar el gráfico
    return graph_json_circular  # Devuelve el JSON

def panel(request):
    print('Retornar panel.html')
    graph_json_barra = generar_grafico_barra(request)
    graph_json_circular = generar_grafico_circular(request)

    return render(request, 'panel.html', {
        'graph_json_barra': graph_json_barra,
        'graph_json_circular': graph_json_circular
    })
