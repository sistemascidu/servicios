# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django import forms

from django.contrib.auth.models import User
from ..models import Solicitud

@login_required(login_url='/entrar/')
def solicitud_list(request):
	items = Solicitud.objects.all().order_by('-fechaSolicitud', '-id')
	lista = { 'titulo' : 'Lista de solicitudes', 'items' : items }
	return render(request, 'servicios/solicitud_list.html', {'lista': lista })

@login_required(login_url='/entrar/')
def solicitud_view(request, idsolicitud='0', modo='v'):
	item = None
	lista = None
	error = ''
	tit = 'Ver solicitud'
	if (modo in ['v', 'e']):
		if (idsolicitud != '0'):
			items = Solicitud.objects.filter(pk=idsolicitud)
			if (items.count() > 0):
				item = items[0]
		else:
			error = 'Debe indicar la solicitud que quiere visualizar'
		if (modo == 'e'):
			tit = 'Editar solicitud'
	return render(request, 'servicios/solicitud_view.html', {'item': item, 'sololectura': modo=='v', 'titulo' : tit})

@login_required(login_url='/entrar/')
def solicitud_add(request):
	item = Solicitud()
	item.usuarioEntrega = request.user
	return render(request, 'servicios/solicitud_view.html', {'item': item, 'titulo' : 'Registrar Solicitud'})

@login_required(login_url='/entrar/')
def crudsolicitud(request):
	direccion = '/'
	if ('g' in request.POST): # guardar item
		op = 'mod'
		if (request.POST['idsolicitud'] == 'None' or request.POST['idsolicitud'] == ''):
			item = Solicitud()
			item.usuarioRecibe = request.user
			op = 'add'
		else:
			items = Solicitud.objects.filter(pk=request.POST['idsolicitud'])
			if (items.count() > 0):
				item = items[0]
		# datos generales
		f = forms.CharField(max_length=200, required=True)
		item.dependencia = f.clean(request.POST['dependencia'])
		item.referencia = f.clean(request.POST['referencia'])
		item.interesado = f.clean(request.POST['interesado'])
		item.fechaSolicitud = request.POST['fechaSolicitud']
		item.tipo = request.POST['tipo']
		# guardamos item
		item.save()
	elif ('m' in request.POST): # modificar 
		if (request.POST['idsolicitud'] != 'None'):
			direccion = '/solicitud/' + request.POST['idsolicitud'] + '/e'
	elif ('b' in request.POST): # borrar 
		if (request.POST['idsolicitud'] != 'None'):
			items = Solicitud.objects.filter(pk=request.POST['idsolicitud'])
			if (items.count() > 0):
				item = items[0]
				item.delete()
	return HttpResponseRedirect(direccion)