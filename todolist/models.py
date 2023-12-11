import imp
from django.db import models
from django.contrib.auth.models import User

class Board(models.Model):
    owner = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
        related_name='owner'
    )
    date = models.DateField()
    title = models.CharField(max_length=128)
    allowed_users = models.ManyToManyField(User, related_name='allowed_users')

class Task(models.Model):
    user = models.ForeignKey(
        User,
        models.SET_NULL,
        blank=True,
        null=True,
    )
    date = models.DateField()
    title = models.CharField(max_length=128)
    description = models.TextField()
    is_finished = models.BooleanField(default=False)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True)