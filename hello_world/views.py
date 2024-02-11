from django.shortcuts import render
from django.http import HttpResponse

def index(request):

    if request.method == 'POST':
        return "You must have POSTed something"
    elif request.ethod == 'GET':
        return HttpResponse(request.method)
