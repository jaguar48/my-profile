from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import status

from django.http import JsonResponse
from rest_framework.decorators import api_view
from .serializers import Caculationserializer
from rest_framework.response import Response

from rest_framework.parsers import JSONParser 

@api_view(['POST','GET'])
def operationlist(request):
   
    serializer = Caculationserializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    y = serializer.validated_data['y']
    x = serializer.validated_data['x']
    operation_type = serializer.validated_data['operation_type']
    
    if operation_type == "addition":
        result = x + y
        
    elif operation_type == "subtraction":
        result = x - y
        
    elif operation_type == "multiplication":
        result = x * y

    context = {
        "slackUsername": "Bishop",
        "operation_type": operation_type,
        "result": result
    }
    return Response(context, status = status.HTTP_200_OK)