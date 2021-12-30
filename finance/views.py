from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from django.utils.http import urlencode

from urllib.parse import urlparse

from authentication.models import User
from .forms import *
from .backends import *


@login_required
def home_page(request):
    if request.method == 'POST':
        return HttpResponseBadRequest()
    else:
        return render(request, 'finance/home.html')


@login_required
def add_transaction_storage_page(request):
    if request.method == 'POST':
        form = AddTransactionStorage(request.POST)
        if form.is_valid():
            add_transaction_storage(owner=request.user, **form.cleaned_data)
            return HttpResponseRedirect('/finance/transaction-storage/get')
    else:
        form = AddTransactionStorage()
    return render(request, 'finance/add_page.html', {'form': form})


@login_required
def get_transaction_storages_page(request):
    if request.method == 'POST':
        if 'id' in request.GET:
            date_range_form = DateRange(request.POST)
            if date_range_form.is_valid():
                dates = date_range_form.cleaned_data
                return HttpResponseRedirect(request.path + '?id=' +
                                            request.GET['id'] + '&' +
                                            urlencode(dates))

        else:
            return HttpResponseBadRequest()
    else:
        if 'id' not in request.GET:
            transaction_storages = get_transaction_storages(owner=request.user)
            if len(transaction_storages) == 0:
                transaction_storages = None
            return render(request, 'finance/get_transactions_storages.html',
                          {'transaction_storages': transaction_storages}
                          )

        now = datetime.datetime.now()

        get_parameters = request.GET.copy().dict()
        if 'start_date' in get_parameters:
            start_date = list(map(int, get_parameters['start_date'].split('-')))
            get_parameters['start_date'] = datetime.date(year=start_date[0], month=start_date[1], day=start_date[2])
        else:
            get_parameters['start_date'] = now.date()

        # start_time = kwargs.get('start_time', now.time()) if self.time is not None else None
        if 'end_date' in get_parameters:
            end_date = list(map(int, get_parameters['end_date'].split('-')))
            get_parameters['end_date'] = datetime.date(year=end_date[0], month=end_date[1], day=end_date[2])
        else:
            get_parameters['end_date'] = now.date() + datetime.timedelta(days=30)
        # end_time = kwargs.get('end_time', now.time())

        transaction_storage = TransactionStorage.objects.get(id=request.GET.get('id'))
        transactions = transaction_storage.get_transactions(**get_parameters)

        date_range_form = DateRange({
            'start_date': request.GET['start_date'],
            'end_date': request.GET['end_date'],
        })

        for transaction in transactions:
            transaction.value /= 100

        return render(request, 'finance/get_transaction_storage_single.html',
                      {'date_range_form': date_range_form,
                       'transaction_storage': transaction_storage,
                       'transactions': transactions, }
                      )


@login_required
def add_transaction_page(request):
    if request.method == 'POST':
        form = AddTransaction(request.POST)
        if form.is_valid():
            meta = (
                {name: int(value) for name, value in
                 (element.split('=') for element in form.data['metadata'].split('&'))})
            add_transaction(owner=request.user, meta=meta, **form.cleaned_data)
            return HttpResponseRedirect('/finance/transaction-storage/get?id=' + str(meta['storage_id']))
    else:
        transaction_storage = TransactionStorage.objects.get(id=request.GET.get('trstid'))
        if 'trstid' not in request.GET or 'trstornu' not in request.GET:
            return HttpResponseBadRequest()
        else:
            try:
                transaction = Transaction.objects.get(storage__id=request.GET.get('trstid'),
                                                      storage_order_number=request.GET.get('trstornu'))
            except ObjectDoesNotExist:
                transaction = Transaction(
                    storage=transaction_storage,
                    storage_order_number=request.GET.get('trstornu'),
                    execution_date=transaction_storage.date,
                    value=transaction_storage.value,
                    is_confirmed=transaction_storage.is_confirmed,
                )
            transaction.execution_date = transaction_storage \
                .get_execution_date(int(transaction.storage_order_number)) \
                .strftime("%Y-%m-%d")
            transaction.value /= 100

            form = AddTransaction(instance=transaction)
            form.data = urlencode(
                {'storage_id': transaction.storage.id, 'storage_order_number': transaction.storage_order_number,
                 'id': transaction.id if transaction.id else -1})
        return render(request, 'finance/add_page.html', {'form': form})


@login_required
def add_target_page(request):
    if request.method == 'POST':
        form = AddTarget(request.POST)
        if form.is_valid():
            add_target(owner=request.user, **form.cleaned_data)
            return HttpResponseRedirect('/finance/target/get')
    else:
        form = AddTarget()
    return render(request, 'finance/add_page.html', {'form': form})


@login_required
def get_targets_page(request):
    if request.method == 'POST':
        return HttpResponseBadRequest()
    else:
        targets = get_targets(owner=request.user)
        if len(targets) == 0:
            targets = None
        return render(request, 'finance/get_targets.html', {'targets': targets})
