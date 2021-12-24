from django.db import models


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
    title = models.TextField(max_length=63)
    description = models.TextField(max_length=1023)
    datetime = models.DateTimeField()
    value = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Транзакция'
        verbose_name_plural = 'Транзакции'
