import imp
from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    date = models.DateField()
    title = models.TextField()
    description = models.TextField()