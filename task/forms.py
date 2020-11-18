from django                 import forms
from .models                import TaskModel


class TaskForm(forms.ModelForm):

    deadline = forms.DateField()

    class Meta:
        model = TaskModel
        fields = ['title','memo', 'priority', 'deadline']

