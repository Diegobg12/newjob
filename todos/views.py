from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
from .models import *
from .permissions import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ListTodoSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    def get_queryset(self):
        user = self.request.user
        return Todo.objects.filter(author=user.id)
    serializer_class = TodoSerializer

class LabelSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = LablesSerializes