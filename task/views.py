from django.shortcuts       import render
from django.views.generic   import (
    ListView,
    DetailView,
    DeleteView,
    UpdateView,
    CreateView,
)
from .models                import TaskModel
from django.urls            import reverse_lazy
from .forms                 import TaskForm


class TaskList(ListView):
    template_name = 'task/list.html'
    model         = TaskModel

class TaskDetail(DetailView):
    template_name = 'task/detail.html'
    model         = TaskModel

class TaskDelete(DeleteView):
    template_name = 'task/delete.html'
    model         = TaskModel
    fields        = ('title', 'memo', 'priority', 'deadline')
    success_url   = reverse_lazy('list')

class TaskUpdate(UpdateView):
    template_name = 'task/update.html'
    model         = TaskModel
    fields        = ('title', 'memo', 'priority', 'deadline')
    success_url   = reverse_lazy('list')

class TaskCreate(CreateView):
    template_name = 'task/create.html'
    model         = TaskModel
    fields        = ('title', 'memo', 'priority', 'deadline')
    success_url   = reverse_lazy('list')