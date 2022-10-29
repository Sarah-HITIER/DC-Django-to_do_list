from django.http import Http404
from django.shortcuts import redirect, render

from todo_list.models import Task
from .forms import TaskForm


def home(request):
    tasks = Task.objects.all()
    context = {
        'tasks': tasks,
    }
    return render(request, 'home.html', context)


def detail(request, pk):
    task = Task.objects.filter(pk=pk)

    if task:
        context = {
            "task": Task.objects.get(pk=pk)
        }
        return render(request, 'detail.html', context)

    raise Http404('This task does not exist')
    # return HttpResponse('This task does not exist')

    # OU :
    # get_object_or_404(Vehicle, pk=pk)
    # context = {
    #     "task": Vehicle.objects.get(pk=pk)
    # }
    # return render(request, 'detail.html', context)


def create(request):
    if request.method == 'POST':
        task_form = TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('home')
    else:
        task_form = TaskForm()

    context = {
        "title": "Create",
        "form": task_form
    }
    return render(request, 'create.html', context)


def update(request, pk):
    task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('detail', pk=pk)
    else:
        form = TaskForm(instance=task)

    context = {
        'title': 'Update',
        'form': form
    }
    return render(request, 'create.html', context)


def delete(request, pk):
    task = Task.objects.get(pk=pk)
    task.delete()
    return redirect('home')
