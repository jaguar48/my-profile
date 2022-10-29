from rest_framework import serializers

from hngapp.models import hng

class hngSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = hng
        fields = ('slackUsername','backend','age','bio')