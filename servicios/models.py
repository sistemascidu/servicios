# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Categoria(models.Model):
	# choices
	lista_tipos = (
		('a', 'Archivo'),
		('f', 'Fondo'),
		('s', 'Sección'),
		('e', 'Serie'),
	)
	# fields
	nombre = models.CharField(max_length = 200)
	descripcion = models.TextField()
	tipo = models.CharField(max_length=1, choices=lista_tipos)
	padre = models.ForeignKey('Categoria', related_name='Jerarquia', blank=True, null=True)
	# methods
	def __unicode__(self):
		return self.getTipoDesc() + ":" + self.nombre
	def getTipoDesc(self):
		d = dict(self.lista_tipos)
		return d[self.tipo]

class Solicitud(models.Model):
	# choices
	lista_tipos = (
		('o', 'Oficio'),
		('c', 'Correo electrónico'),
		('t', 'Teléfono'),
	)
	# fields
	dependencia = models.CharField(max_length = 200)
	tipo = models.CharField(max_length = 1, choices = lista_tipos)
	referencia = models.CharField(max_length = 200, blank=True, null=True)
	interesado = models.CharField(max_length = 200)
	fechaSolicitud = models.DateField()
	usuarioRecibe = models.ForeignKey('auth.User', related_name='sol_recibe')
	fechaRecibe = models.DateField(auto_now_add=True)
	# methods
	def getTipoDesc(self):
		d = dict(self.lista_tipos)
		return d[self.tipo]
	def getEnlaceServicio(self):
		enlace = '/servicio/' + str(self.id)
		results = Servicio.objects.filter(solicitud_id=self.id)
		if (len(results) > 0):
			enlace = '/servicio/' + str(results[0].id) + '/v'
		return enlace

class Servicio(models.Model):
	# choices
	lista_tipos = (
		('p', 'Préstamo'),
		('c', 'Copia'),
		('o', 'Consulta'),
	)
	# fields
	expediente = models.CharField(max_length = 200)
	destinatario = models.CharField(max_length = 200)
	fondo = models.ForeignKey('Categoria', related_name='fondo')
	seccion = models.ForeignKey('Categoria', related_name='seccion', blank=True, null=True)
	serie = models.ForeignKey('Categoria', related_name='serie', blank=True, null=True)
	fechaEntrega = models.DateField(auto_now_add=True)
	fechaDevolucion = models.DateField(blank=True, null=True)
	tipo = models.CharField(max_length=1, choices=lista_tipos)
	usuarioEntrega = models.ForeignKey('auth.User', related_name='usr_prestamo')
	usuarioRecibe = models.ForeignKey('auth.User', related_name='usr_recibe', blank=True, null=True)
	oficio = models.CharField(max_length = 20, blank=True, null=True)
	solicitud = models.ForeignKey(Solicitud, related_name='servicio_solicitud')
	# methods
	def getTipoDesc(self):
		d = dict(self.lista_tipos)
		return d[self.tipo]
	def getSecciones(self):
		return Categoria.objects.filter(tipo='s')
	def getSeries(self):
		return Categoria.objects.filter(tipo='e')

class UsuarioCategoria(models.Model):
	# fields
	usuario = models.ForeignKey('auth.User', related_name='usuario_categoria')
	categoria = models.ForeignKey('Categoria', related_name='categoria_usuario')
	# methods
	def __unicode__(self):
		return self.usuario.first_name + ': ' + self.categoria.nombre
