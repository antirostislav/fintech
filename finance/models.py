from django.db import models

from authentication.models import User


class Transaction(models.Model):
    """
    Класс расхода
    """
    title = models.TextField()
    datetime = models.DateTimeField()
    value = models.IntegerField()


class Target(models.Model):
    """
    Класс цели
    """
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.TextField(max_length=63)
    description = models.TextField(max_length=1023)
    date = models.DateField()
    time = models.TimeField(null=True)
    value = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'
