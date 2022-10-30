from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import hngSerializer
from .models import hng


class hngViewSet(viewsets.ModelViewSet):
    queryset = hng.objects.all()
    serializer_class = hngSerializer
    
