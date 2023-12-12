from django.forms import ModelForm, Form, CharField
from .models import Task, Board

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description']

class BoardForm(ModelForm):
    class Meta:
        model = Board
        fields = ['title']

class InviteUserForm(Form):
    invited_username = CharField(max_length=150)