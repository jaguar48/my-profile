from rest_framework import serializers

from .models import Caculations

class Caculationserializer(serializers.ModelSerializer):
    class Meta:
        model = Caculations
        fields = "__all__"