from rest_framework import serializers

from hngapp.models import hng
from rest_framework.response import Response


class hngSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = hng
        fields = ('slackUsername','backend','age','bio')

def get(self):
    return Response(hngSerializer)