import datetime

from django import forms
from django.core.exceptions import PermissionDenied
from django.utils.http import parse_http_date

from .models import *


def get_transaction_storages(owner) -> list[TransactionStorage]:
    transaction_storages = list(TransactionStorage.objects.filter(owner=owner))

    for transaction_storage in transaction_storages:
        transaction_storage.value /= 100

    return transaction_storages


def add_transaction_storage(owner, **kwargs) -> None:
    kwargs.setdefault('is_repeated', False)
    kwargs.setdefault('is_confirmed', False)
    kwargs.setdefault('frequency', 30)
    kwargs.setdefault('owner', owner)

    kwargs['value'] = int(kwargs['value'] * 100)

    if not kwargs.pop('is_repeated'):
        kwargs['frequency'] = None
    else:
        kwargs['frequency'] = datetime.timedelta(days=kwargs.pop('frequency'))

    TransactionStorage.objects.create(**kwargs)


def add_transaction(owner, meta, **kwargs):
    kwargs.setdefault('is_confirmed', False)
    kwargs.setdefault('storage_id', meta['storage_id'])
    kwargs.setdefault('storage_order_number', meta['storage_order_number'])
    # kwargs.setdefault('owner', owner)

    transaction_storage = TransactionStorage.objects.get(id=meta['storage_id'])
    if transaction_storage.owner == owner:

        kwargs['value'] = int(kwargs['value'] * 100)

        if meta['id'] == -1:
            Transaction.objects.create(**kwargs)
        else:
            kwargs.setdefault('id', meta['id'])
            Transaction(**kwargs).save()
    else:
        raise PermissionDenied()


def get_targets(owner) -> list[Target]:
    targets = list(Target.objects.filter(owner=owner))

    for target in targets:
        target.value /= 100

    return targets


def add_target(owner, **kwargs) -> None:
    kwargs.setdefault('has_time', False)
    kwargs.setdefault('owner', owner)

    kwargs['value'] = int(kwargs['value'] * 100)

    if not kwargs.pop('has_time'):
        kwargs['time'] = None

    Target.objects.create(**kwargs)
