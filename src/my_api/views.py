from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

# Create your views here.


def api(request):
	name = request.GET['name']
	info = request.GET['info']
	data = {
		'name': name.upper(),
		'info': info.upper()
	}
	return JsonResponse(data)