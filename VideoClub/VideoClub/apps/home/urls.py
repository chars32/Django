#from django.conf.urls.defaults import patterns, url
from django.conf.urls import patterns, include, url

urlpatterns = patterns('VideoClub.apps.home.views',
	url(r'^prueba/$', 'prueba', name="vista_prueba"),
	url(r'^actores/$', 'vista_actores', name="vista_actores"),
	 #url(r'^time/plus/(\d+)/$', 'hours_ahead'),
	url(r'^pelis/(\d+)/$', 'vista_date', name='vista_pelis'),
	)