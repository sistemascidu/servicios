# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django import forms

from django.contrib.auth.models import User
from ..models import Categoria, Servicio, UsuarioCategoria, Solicitud

# actualizaciones
@login_required(login_url='/entrar/')
def servicio_list(request):
	items = Servicio.objects.all().order_by('-fechaEntrega', '-id')
	lista = { 'titulo' : 'Lista de servicios', 'items' : items }
	return render(request, 'servicios/servicio_list.html', {'lista': lista })

@login_required(login_url='/entrar/')
def servicio_view(request, idservicio='0', modo='v'):
	item = None
	lista = None
	dev = True
	error = ''
	tit = 'Ver servicio'
	if (modo in ['v', 'e']):
		if (idservicio != '0'):
			items = Servicio.objects.filter(pk=idservicio)
			if (items.count() > 0):
				item = items[0]
		else:
			error = 'Debe indicar el servicio que quiere visualizar'
		if (modo == 'e'):
			lista = getFondosUsuarios(request.user.id)
			dev = False
			tit = 'Editar servicio'
	return render(request, 'servicios/servicio_view.html', {'item': item, 'sololectura': modo=='v', 'dev' : dev, 'titulo' : tit, 'lista_fondos' : lista})

@login_required(login_url='/entrar/')
def servicio_print(request, idservicio='0'):
	item = None
	items = Servicio.objects.filter(pk=idservicio)
	if (items.count() > 0):
		item = items[0]
	return render(request, 'servicios/servicio_print.html', {'item': item })

@login_required(login_url='/entrar/')
def servicio_add(request, idsolicitud='0'):
	sol = None
	results = Solicitud.objects.filter(pk=idsolicitud)
	if (results.count() > 0):
		sol = results[0]
		item = Servicio()
		item.solicitud = sol
		item.usuarioEntrega = request.user
		lista = getFondosUsuarios(request.user.id)
		return render(request, 'servicios/servicio_view.html', {'item': item, 'lista_fondos' : lista, 'dev' : False, 'titulo' : 'Registrar Servicio'})
	else:
		error = 'Debe indicar el servicio que quiere visualizar'

@login_required(login_url='/entrar/')
def servicio_dev(request):
	return render(request, 'servicios/servicio_dev.html', {})

@login_required(login_url='/entrar/')
def crudservicio(request):
	direccion = '/'
	if ('g' in request.POST): # guardar item
		op = 'mod'
		if (request.POST['idservicio'] == 'None' or request.POST['idservicio'] == ''):
			item = Servicio()
			item.usuarioEntrega = request.user
			op = 'add'
		else:
			items = Servicio.objects.filter(pk=request.POST['idservicio'])
			if (items.count() > 0):
				item = items[0]
		# datos generales
		f = forms.CharField(max_length=200, required=True)
		item.expediente = f.clean(request.POST['expediente'])
		item.destinatario = f.clean(request.POST['destinatario'])
		item.oficio = f.clean(request.POST['oficio'])
		item.tipo = request.POST['tipo']
		item.fondo = Categoria.objects.get(id=request.POST['fondo'])
		item.solicitud = Solicitud.objects.get(pk=request.POST['solicitud'])
		if (request.POST['seccion'] and request.POST['seccion']!='-'):
			item.seccion = Categoria.objects.get(id=request.POST['seccion'])
		if (request.POST['serie'] and request.POST['serie']!='-'):
			item.seccion = Categoria.objects.get(id=request.POST['serie'])
		# guardamos item
		item.save()
		# vamos a imprimir si se acaba de crear
		direccion = '/imprimir/' + str(item.id)
	elif ('m' in request.POST): # modificar 
		if (request.POST['idservicio'] != 'None'):
			direccion = '/servicio/' + request.POST['idservicio'] + '/e'
	elif ('b' in request.POST): # borrar 
		if (request.POST['idservicio'] != 'None'):
			items = Servicio.objects.filter(pk=request.POST['idservicio'])
			if (items.count() > 0):
				item = items[0]
				item.delete()
	elif ('d' in request.POST): # devolver
		dev = False
		if (request.POST['idservicio'] != None):
			items = Servicio.objects.filter(pk=request.POST['idservicio'])
			if (items.count() > 0):
				item = items[0]
				if (item.tipo == 'p' and item.usuarioRecibe == None):
					item.usuarioRecibe = request.user
					item.fechaDevolucion = datetime.date.today()
					item.save()
					dev = True
	elif ('i' in request.POST): #imprimir
		direccion = '/imprimir/' + request.POST['idservicio']
	return HttpResponseRedirect(direccion)


# funciones auxiliares
def getFondosUsuarios(idUsuario):
	rel = UsuarioCategoria.objects.filter(usuario__id=idUsuario)
	fondos = []
	for f in rel:
		fondos.append(f.categoria.id)
	lista = Categoria.objects.filter(tipo='f', id__in=fondos)
	return lista
