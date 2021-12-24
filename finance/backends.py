from django import forms

from .models import *


def get_transactions(form: forms.Form) -> list[Transaction]:
    pass


def add_transaction(form: forms.Form) -> forms.Form:
    data = form.clean()

    if not form.errors:
        Transaction(data).save()
    return form


def get_targets() -> list[Target]:
    return list(Target.objects.all())


def add_target(form: forms.Form) -> forms.Form:
    data = form.clean()

    if not form.errors:
        data['value'] = int(data['value'] * 100)
        Target.objects.create(**data)
    return form
