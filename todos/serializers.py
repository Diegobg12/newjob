from rest_framework import serializers
from .models import *

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Todo
        fields = (
            'id', 
            'title', 
            'notes', 
            'startDate', 
            'dueDate', 
            'completed', 
            'starred', 
            'important',
            'deleted',
            'labels',
            'author')
        read_only_fields = ('author',)

class LablesSerializes(serializers.ModelSerializer):
    class Meta:
        model= Label
        fields = (
            'title',
            'handle',
            'color'
        )
        