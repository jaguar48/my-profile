from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from django.http import JsonResponse

def myhng(request):
    my_data = {'slackUsername':'Bishop','backend':True,'age':25,'bio':'I am a programmer'}
    return JsonResponse(my_data)
    
