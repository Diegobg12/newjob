from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Todo
        fields = ('__all__')
        read_only_fields = ('startDate',)

class LablesSerializes(serializers.ModelSerializer):
    class Meta:
        model= Label
        fields = (
            'title',
            'handle',
            'color'
        )
        