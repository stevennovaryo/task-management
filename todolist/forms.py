from django.forms import ModelForm
from .models import Task, Board

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title']