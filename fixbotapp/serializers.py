from rest_framework import serializers
from .models import TelemetricModel

class TelemetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelemetricModel
        fields = '__all__'