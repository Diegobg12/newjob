from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .models import *
from .serializers import *

# Create your views here.

class ListTodoSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class LabelSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = LablesSerializes