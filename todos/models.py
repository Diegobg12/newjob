from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.db import models
from datetime import datetime
# Create your models here.

class Label(models.Model):
    handle = models.CharField(max_length=20, null=True, blank= True)
    title = models.CharField(max_length=20, null=True, blank= True)
    color = models.CharField(max_length=20, null=True, blank= True)
    def __str__(self):
        return self.title
        
class Todo(models.Model):
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True, blank= True)
    notes = models.TextField(max_length=250, null=True, blank= True)
    startDate = models.DateField(default=datetime.now, auto_created=True)
    dueDate = models.DateField(default=datetime.now, null=True, blank= True)
    completed= models.BooleanField(default = False, null=True, blank= True)
    starred= models.BooleanField(default = False, null=True, blank= True)
    important= models.BooleanField(default = False, null=True, blank= True)
    deleted= models.BooleanField(default = False, null=True, blank= True)
    labels =  models.ManyToManyField(Label, related_name="labels", blank= True)
    def __str__(self):
        return self.title

