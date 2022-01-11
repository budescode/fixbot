from rest_framework import serializers
from .models import TelemetricModel

#the serializer for the data, we will use all fields.
class TelemetricSerializer(serializers.ModelSerializer):
    class Meta:
        model = TelemetricModel
        fields = '__all__'