from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('<int:pk>/',DetailTodo.as_view()),
    path('',ListTodo.as_view())
]
