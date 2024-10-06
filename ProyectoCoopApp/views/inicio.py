from urllib import response
#from django.http import HttpResponse
#from django.template import Template, Context
#from django.template.loader import get_template
from django.shortcuts import render
import requests


def index(request):
    print('Retornar pagina index.html')
    return render(request, 'index.html',)