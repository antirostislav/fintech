import datetime

from django.db import models

from authentication.models import User
from fintech import settings


class TransactionStorage(models.Model):
    """
    Класс хранения транзакций
    """
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=63)
    description = models.TextField(max_length=1023, null=True)
    date = models.DateField()
    # time = models.TimeField(null=True)
    frequency = models.DurationField(null=True)
    value = models.BigIntegerField()
    is_confirmed = models.BooleanField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    def get_execution_date(self, order_number):
        counter = 0
        date = self.date
        while counter < order_number:
            date += self.frequency
            counter += 1
        return date

    def get_transactions(self, **kwargs):
        if self.frequency is None:
            return list(Transaction.objects.get(storage=self))
        else:

            edited_transactions = Transaction.objects \
                .filter(storage=self, execution_date__range=(kwargs['start_date'], kwargs['end_date'])) \
                .order_by('execution_date')
            prepared_transactions = {}
            for transaction in edited_transactions:
                prepared_transactions[transaction.storage_order_number] = transaction
            ready_transactions = []

            order_number = 0
            date = self.date
            while date < kwargs['start_date']:
                date += self.frequency
                order_number += 1

            while date <= kwargs['end_date']:
                if order_number not in prepared_transactions.keys():
                    ready_transactions.append(Transaction(
                        storage=self,
                        storage_order_number=order_number,
                        execution_date=date,
                        value=self.value,
                        is_confirmed=self.is_confirmed,
                    ))
                else:
                    ready_transactions.append(prepared_transactions[order_number])

                date += self.frequency
                order_number += 1

            return ready_transactions

        # ready_transactions = []
        # ready_transactions = []
        #
        # edited_transactions = Transaction.objects \
        #     .filter(storage=self, expected_execution_date__range=(start_date, end_date)) \
        #     .order_by('expected_execution_date')
        #
        # transaction_pointer = 0
        # date = self.date
        # while date < start_date:
        #     date += self.frequency
        #
        # while date <= end_date:
        #     if len(edited_transactions) > 0 and \
        #             edited_transactions[transaction_pointer].expected_execution_date == date:
        #         ready_transactions.append(edited_transactions[transaction_pointer])
        #         transaction_pointer += 1
        #     else:
        #         ready_transactions.append(Transaction(
        #             storage=self,
        #             expected_execution_date=date,
        #             actual_execution_date=date,
        #             value=self.value,
        #             is_confirmed=self.is_confirmed,
        #         ))
        #
        #     next_date = date
        #     next_date += self.frequency
        #     next_date = next_date if next_date < end_date else end_date
        #
        #     for prepared_transaction in ready_transactions:
        #         if date <= prepared_transaction.actual_execution_date <= end_date and \
        #                 prepared_transaction < next_date:
        #             ready_transactions.append(prepared_transaction)
        #             prepared_transaction.delete(prepared_transaction)
        #
        #     date += self.frequency
        #
        # return ready_transactions


class Transaction(models.Model):
    """
    Класс транзакции
    """
    storage = models.ForeignKey(TransactionStorage, on_delete=models.CASCADE)
    storage_order_number = models.PositiveIntegerField()
    execution_date = models.DateField()
    # time = models.TimeField(null=True)
    value = models.PositiveBigIntegerField()
    is_confirmed = models.BooleanField()
    created_datetime = models.DateTimeField(auto_now_add=True)


class Target(models.Model):
    """
    Класс цели
    """
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    title = models.TextField(max_length=63)
    description = models.TextField(max_length=1023)
    date = models.DateField()
    time = models.TimeField(null=True)
    value = models.PositiveBigIntegerField()
    created_datetime = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цели'
