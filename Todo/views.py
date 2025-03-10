from django.shortcuts import render, redirect
from .models import Task
from .forms import UserForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
    
def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'todo/account/register.html', {'form': form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('task_list')
    
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(f"✅ {user.username} đã đăng nhập")  # In log để kiểm tra
            return redirect('task_list')
    else:
        form = AuthenticationForm()
    return render(request, 'todo/account/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)
    return render(request, 'todo/task_list.html', {'tasks': tasks})
    
@login_required
def add_task(request):
    if request.method == 'POST':
        title = request.POST['task']
        description = request.POST['description']
        user = request.user
        task = Task(title=title, description=description, user=user)
        task.save()
        return redirect('task_list')
    return render(request, 'todo/add_task.html')

@login_required
def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST['task']
        description = request.POST['description']
        task.title = title
        task.description = description
        task.user = request.user
        task.save()
        return redirect('task_list')
    return render(request, 'todo/edit_task.html', {'task': task})

@login_required
def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    if task.user != request.user:
        return redirect('task_list')
    task.delete()
    return redirect('task_list')

@login_required
def complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.complete = True
    task.user = request.user
    task.save()
    return redirect('task_list')