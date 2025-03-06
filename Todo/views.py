from django.shortcuts import render, redirect
from .models import Task
    
def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})
    
def add_task(request):
    if request.method == 'POST':
        title = request.POST['task']
        description = request.POST['description']
        task = Task(title=title, description=description)
        task.save()
        return redirect('task_list')
    return render(request, 'todo/add_task.html')

def edit_task(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        title = request.POST['task']
        description = request.POST['description']
        task.title = title
        task.description = description
        task.save()
        return redirect('task_list')
    return render(request, 'todo/edit_task.html', {'task': task})

def delete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('task_list')

def complete_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.complete = True
    task.save()
    return redirect('task_list')