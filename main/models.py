from django.db import models


# Create your models here.

class Task(models.Model):
    title = models.CharField('Название', max_length=150)
    text = models.TextField('Текст')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'
