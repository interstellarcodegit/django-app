from rest_framework import serializers
from .models import Updates 

class UpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model= Updates
        fields= '__all__'
        