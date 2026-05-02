from django.shortcuts import render, redirect
from django.http import HttpResponse
#from os import name
#import json
#import requests




def index(request):
    
    return render(request, 'index.html')


