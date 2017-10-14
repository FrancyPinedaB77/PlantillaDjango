# Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from django.http import JsonResponse
import os
import sys
import json 
import glob


reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

def inicio(request):
    return render(request, 'inicio.html')


def index(request):
    return render(request, "index.html", {})


def grafo(request):
    return render(request, "grafo.html")

def taller3(request):
    return render(request, "taller3.html")