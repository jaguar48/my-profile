from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from .serializers import hngSerializer
from .models import hng
from django.http import JsonResponse


# class hngViewSet(viewsets.ModelViewSet):
#     queryset = hng.objects.all()
#     serializer_class = hngSerializer
#     return serializer_class.json()


@api_view(['GET'])
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = hng.objects.all()
        serializer = hngSerializer(snippets, many=True)
        return JsonResponse(serializer.data)