from django.db import models

# カラー：優先度
PRIORITY = (('danger', 'High'), ('info', 'Normal'), ('success', 'Low'))


class TaskModel(models.Model):
    title    = models.CharField(max_length=128)
    memo     = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices=PRIORITY
    )
    deadline = models.DateField()

    def __str__(self):
        return self.title
