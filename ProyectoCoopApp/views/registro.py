from urllib import response
from hashlib import algorithms_available, pbkdf2_hmac, sha256
from django.shortcuts import render
from django.contrib.auth.models import User
from ProyectoCoopApp.models import Usuario
from datetime import datetime
import requests


def registro(request):
    print('Retornar pagina registro.html')
    return render(request, 'registro.html',)

def formulario_registro(request):
    print('Retornar pagina registro.html')

    if request.method == 'GET':
        print('invocación por método GET')
        run = request.GET.get('nombre')
        print('run {0}'.format(nombre))

        
    elif request.method == 'POST': 
        print('invocación por método POST')
        rut = request.POST.get('rut')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        usuario = request.POST.get('usuario')
        clave = request.POST.get('clave')
        
        
        #Guardar en la Base de datos Socios
        user = Usuario()
        user.nombre_soc = nombre
        user.apellido_soc = apellido
        user.rut_soc = rut
        user.correo_soc = correo
        user.usuario_soc = usuario
        user.clave_soc = clave
        user.save()

        #Guardar en el auth
        new_user = User() 
        new_user.first_name = nombre
        new_user.last_name = apellido
        new_user.email = correo
        new_user.username = usuario
        new_user.set_password(clave)
        new_user.is_superuser = 1
        new_user.is_staff = 1
        new_user.is_active = 1
        new_user.date_joined = datetime.today()
        new_user.save()

        # Imprimir los datos 
        print('rut {0}'.format(rut))
        print('nombre {0}'.format(nombre))
        print('apellido{0}'.format(apellido))
        print('correo{0}'.format(correo))
        print('usuario {0}'.format(usuario))
        print('clave {0}'.format(clave))



    return render(request, 'registro.html')