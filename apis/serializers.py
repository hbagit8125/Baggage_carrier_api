
from rest_framework import serializers
from .models import carrier

class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = carrier
        fields = ('__all__')