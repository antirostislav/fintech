from django import forms

from .models import *


def get_transactions(form: forms.Form) -> list[Transaction]:
    pass


def add_transaction(form: forms.Form) -> forms.Form:
    data = form.clean()

    if not form.errors:
        Transaction(data).save()
    return form


def get_targets(owner) -> list[Target]:
    return list(Target.objects.filter(owner=owner))


def add_target(owner, **kwargs) -> None:
    kwargs.setdefault('has_time', False)
    kwargs.setdefault('owner', owner)

    kwargs['value'] = int(kwargs['value'] * 100)

    if not kwargs.pop('has_time'):
        kwargs['time'] = None
    Target.objects.create(**kwargs)
