# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

# ingresar al sistema
def user_login(request):
	items = []
	return render(request, 'servicios/entrar.html', {'datos': items})
def entrar(request):
	u = request.POST['username']
	p = request.POST['password']
	user = authenticate(username=u, password=p)
	if user is None:
	    # No backend authenticated the credentials
	    return render(request, 'servicios/entrar.html', {
            'error_message': "El usuario no existe o la contraseña no es correcta.",
        })
	else:
	    # a backend authenticated the credentials
	    login(request, user)
	    return HttpResponseRedirect('/')
def salir(request):
    logout(request)
    return HttpResponseRedirect('/entrar/')