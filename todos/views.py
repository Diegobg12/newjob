from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, permissions, viewsets
from .permissions import *
from .models import *
from .serializers import *

# Create your views here.

class ListTodoSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,permissions.IsAuthenticated)
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(author=user)
    serializer_class = TodoSerializer

class LabelSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = LablesSerializes