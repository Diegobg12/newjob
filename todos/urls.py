from django.contrib import admin
from rest_framework.routers import SimpleRouter
from django.urls import path, include
from .views import *


router = SimpleRouter()
router.register('', ListTodoSet,basename= 'todos')
router.register('labels', LabelSet,basename= 'labels')
urlpatterns = router.urls
