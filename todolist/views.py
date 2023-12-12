from multiprocessing import context
from sqlite3 import Date
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import datetime
from django.urls import reverse
from urllib3 import HTTPResponse
from .models import Task, Board
from .forms import TaskForm, BoardForm, InviteUserForm
from django.contrib.auth.models import User

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
            return HttpResponseRedirect(reverse('todolist:show_boardlist'))
    else:
        form = TaskForm()
    return render(request, 'create_task.html', {'form': form})

@login_required(login_url='/todolist/login/')
def add_task(request, board_id):
    if request.method != 'POST':
        return redirect('todolist:amogus')
    
    form = TaskForm(request.POST)
    if form.is_valid():
        new_task = form.save(commit=False)
        new_task.user = request.user
        new_task.date = datetime.datetime.now()
        board = Board.objects.get(id=board_id)
        new_task.board = board
        new_task.save()
        form.save_m2m()
        return HttpResponse(serializers.serialize('json', [new_task, ]), content_type='application/json')

@login_required(login_url='/todolist/login/')
def finish_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if task.user == request.user:
        task.is_finished = True
        task.save()
    else:
        return redirect(reverse('todolist:amogus'))
    board_id = request.GET.get('board_id')
    return redirect(reverse('todolist:show_board', kwargs={'board_id': board_id}))

@login_required(login_url='/todolist/login/')
def unfinish_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if task.user == request.user:
        task.is_finished = False
        task.save()
    else:
        return redirect(reverse('todolist:amogus'))

    board_id = request.GET.get('board_id')
    return redirect(reverse('todolist:show_board', kwargs={'board_id': board_id}))

@login_required(login_url='/todolist/login/')
def delete_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    if task.user == request.user:
        task.delete()
    else:
        return redirect(reverse('todolist:amogus'))

    board_id = request.GET.get('board_id')
    return redirect(reverse('todolist:show_board', kwargs={'board_id': board_id}))

@login_required(login_url='/todolist/login/')
def delete_task_ajax(request, task_id):
    task = Task.objects.get(pk=task_id)

    if task.user == request.user:
        task.delete()
    else:
        return redirect(reverse('todolist:amogus'))

    return HttpResponse(serializers.serialize('json', [task, ]), content_type='application/json')

def show_task(request, task_id):
    task = Task.objects.get(pk=task_id)

    return render(request, 'show_task.html', context={'task':task})

@login_required(login_url='/todolist/login/')
def get_task_json(request):
    board_id = request.GET.get('board_id')
    data = Task.objects.filter(board__id=board_id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


# Board
@login_required(login_url='/todolist/login/')
def show_boardlist(request):
    board_list = Board.objects.filter(allowed_users=request.user)

    context = {
        'username': request.user.username,
        'board_list': board_list,
    }

    return render(request, 'boardlist.html', context)

@login_required(login_url='/todolist/login/')
def add_board(request):
    if request.method != 'POST':
        return redirect('todolist:amogus')
    
    form = BoardForm(request.POST)
    if form.is_valid():
        new_board = form.save(commit=False)
        new_board.owner = request.user
        new_board.date = datetime.datetime.now()
        new_board.save()
        new_board.allowed_users.add(new_board.owner)
        form.save_m2m()
        return HttpResponse(serializers.serialize('json', [new_board, ]), content_type='application/json')

@login_required(login_url='/todolist/login/')
def get_board_json(request):
    data = Board.objects.filter(allowed_users=request.user)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

@login_required(login_url='/todolist/login/')
def show_board(request, board_id):
    board = Board.objects.get(pk=board_id)

    if not board.allowed_users.filter(id=request.user.id).exists():
        return redirect(reverse('todolist:amogus'))

    task_list = Task.objects.filter(board=board)

    context = {
        'username': request.user.username,
        'task_list': task_list,
        'board': board,
    }

    return render(request, 'todolist.html', context)

@login_required(login_url='/todolist/login/')
def invite_user(request):
    if request.method != 'POST':
        return redirect('todolist:amogus')
    
    form = InviteUserForm(request.POST)
    if form.is_valid():
        try:
            invited_username = form.cleaned_data["invited_username"]
            invited_user = User.objects.get(username=invited_username)
            
            board_id = request.POST.get('board_id')
            board = Board.objects.get(pk=board_id)
            board.allowed_users.add(invited_user)
        except:
            print('User not found')
            pass
        
    return redirect(reverse('todolist:show_board', kwargs={'board_id': 1}))

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
            response = HttpResponseRedirect(reverse("todolist:show_boardlist")) # membuat response
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
    return redirect('todolist:show_boardlist')