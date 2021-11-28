from django.db import models


class Expense:
    """
    Класс расхода
    """
    uid: models.IntegerField()
    title: models.TextField()
    datetime: models.DateTimeField()
    value: models.IntegerField()


class Income:
    """
    Класс дохода
    """
    uid: models.IntegerField()
    title: models.TextField()
    datetime: models.DateTimeField()
    value: models.IntegerField()


class Goal:
    """
    Класс цели
    """
    uid: models.IntegerField()
    title: models.TextField()
    datetime: models.DateTimeField()
    value: models.IntegerField()
