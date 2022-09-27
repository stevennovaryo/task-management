from multiprocessing import context
from sqlite3 import Date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime
from django.urls import reverse
from .models import Task
from .forms import TaskForm

@login_required(login_url='/todolist/login/')
def show_todolist(request):
    task_list = Task.objects.filter(user=request.user)

    context = {
        'username': request.user.username,
        'task_list': task_list,
    }

    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.date = datetime.datetime.now()
            new_task.save()
            form.save_m2m()
            return HttpResponseRedirect(reverse('todolist:show_todolist'))
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

@login_required(login_url='/todolist/login/')
def finish_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if task.user == request.user:
        task.is_finished = True
        task.save()
    else:
        return redirect(reverse('todolist:amogus'))

    return redirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def unfinish_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if task.user == request.user:
        task.is_finished = False
        task.save()
    else:
        return redirect(reverse('todolist:amogus'))

    return redirect(reverse('todolist:show_todolist'))

@login_required(login_url='/todolist/login/')
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if task.user == request.user:
        task.delete()
    else:
        return redirect(reverse('todolist:amogus'))

    return redirect(reverse('todolist:show_todolist'))

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Akun telah berhasil dibuat!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user) # melakukan login terlebih dahulu
            response = HttpResponseRedirect(reverse("todolist:show_todolist")) # membuat response
            response.set_cookie('last_login', str(datetime.datetime.now())) # membuat cookie last_login dan menambahkannya ke dalam response
            return response
        else:
            messages.info(request, 'Username atau Password salah!')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    return redirect('todolist:login')

def amogus(request):
    return render(request, 'amogus.html')

def test(request, message):
    print(message)
    return redirect('todolist:show_todolist')