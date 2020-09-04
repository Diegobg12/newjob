from django.db import models
from django.db import models
from datetime import datetime
# Create your models here.

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    dateCreated = models.DateField(default=datetime.now)
    dueDate = models.DateField()

    def __str__(self):
        return self.title
