from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from main.forms import TaskForm
from main.models import Task


def index(request):
    task = Task.objects.all()
    users = User.objects.all()

    return render(request, 'main/index.html', {'task': task, 'users': users})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    users = User.objects.all()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            error = 'Форма неверная'

    form = TaskForm()
    context = {'form': form, 'error': error}
    return render(request, 'main/create.html', context)
