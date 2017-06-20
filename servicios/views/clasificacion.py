# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User
from ..models import Categoria
from django.core import serializers
import json

# actualizaciones
@login_required(login_url='/entrar/')
def categorias_list(request):
	# archivos
	items = getItemNode()
	l = json.dumps(items, ensure_ascii=False).encode("utf8")
	return render(request, 'servicios/clasificacion.html', {'lista': l })

def getItemNode(id = None, name = 'CIDU', itemtype = 'Clasificación'):
	item = {
		'name' : name.replace('"', ''),
		'type' : itemtype,
		'children' : [],
	}
	#if (itemtype in ['Archivo', 'Fondo', 'Sección', 'Serie']):
	#	item['collapsed'] = 'true'
	children = Categoria.objects.filter(padre=id)
	for child in children:
		item['children'].append(getItemNode(child.id, child.nombre, child.getTipoDesc()))
	return item