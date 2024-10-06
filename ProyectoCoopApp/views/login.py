from urllib import response
from django.shortcuts import render
from django.contrib.auth.models import User
from ProyectoCoopApp.models import Usuario
from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, authenticate
import requests


#def login(request):
#    print('Retornar pagina login.html')
#    return render(request, 'login.html',)

def login(request):
    print('login.index')
    if request.method == 'POST':
        print('request.method: ',  request.method)        
        try:
            username = request.POST.get('usuario')
            password = request.POST.get('clave')
            print('username: ',  username)        
            print('password: ',  password)                    
            user = authenticate(username=username, password=password)
            print('authenticated: ',  True)                                            
            auth_login(request, user)
            print('login: ',  True)                                
            return redirect('/index')
        except Exception as e:
            print(e)        
    return render(request, 'login.html')

def authorization(request, perm):
    print('authorization | user -> ', request.user)
    if request.user != None and request.user.__str__() != 'AnonymousUser':
        if request.user.has_perm(perm):
            return True, ''
        else:
            return False, '/error-403/'
    else:
        print('Unauthorized')
        return False, '/error-401/'