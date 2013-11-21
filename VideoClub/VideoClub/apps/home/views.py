from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import *

def prueba(request):
	html = '<body><p>Hola</p></body>'	
	return HttpResponse(html)

def vista_actores(request):
	actores = Actor.objects.all().order_by('nombre')
	#return HttpResponse(pelicula)
	return render_to_response('actor.html', {'actores':actores }, context_instance=RequestContext(request))

def vista_date(request, offset):
	offset = int(offset)
	pelicula = Pelicula.objects.all()
	return render_to_response('pelis.html', {'pelicula':pelicula, 'anio':offset}, context_instance=RequestContext(request))