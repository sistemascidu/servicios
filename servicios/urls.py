from django.conf.urls import url
from servicios import views

urlpatterns = [
	# ingreso al sistema
    url(r'^entrar/$', views.user_login), 
    url(r'^ingresar/$', views.entrar), 
    url(r'^salir/$', views.salir), 
    # servicio
    url(r'^servicio/(?P<idsolicitud>[0-9]+)$', views.servicio_add, name='registro_servicio'),
    url(r'^servicio/(?P<idservicio>[0-9]+)/(?P<modo>[a-z])$', views.servicio_view, name='ver_servicio'),
    url(r'^imprimir/(?P<idservicio>[0-9]+)$', views.servicio_print, name='imp_servicio'),
    url(r'^servicios/$', views.servicio_list, name='ver_servicios'),
    url(r'^crudservicio/$', views.crudservicio), 
    # solicitud 
    url(r'^solicitud/$', views.solicitud_add, name='registro_solicitud'),
    url(r'^solicitud/(?P<idsolicitud>[0-9]+)/(?P<modo>[a-z])$', views.solicitud_view, name='ver_solicitud'),
    url(r'^$', views.solicitud_list, name='ver_solicitudes'),
    url(r'^crudsolicitud/$', views.crudsolicitud), 
    # clasificacion
    url(r'^clasificacion/$', views.categorias_list)
]