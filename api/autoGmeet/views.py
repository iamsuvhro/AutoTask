from urllib import request
from django.shortcuts import render,HttpResponse

# Create your views here.
def createTask(request):
    return HttpResponse("Api will create here",request)