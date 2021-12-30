import datetime

from django import forms

from .models import Transaction


class DateRange(forms.Form):
    form_name = 'Выбрать период'
    button_text = 'Показать'

    start_date = forms.DateField(
        label='',
        initial=datetime.date.today().strftime("%Y-%m-%d"),
        widget=forms.DateInput(attrs={
            'type': 'date',
        }),
    )

    end_date = forms.DateField(
        label='',
        initial=(datetime.date.today() + datetime.timedelta(days=30)).strftime("%Y-%m-%d"),
        widget=forms.DateInput(attrs={
            'type': 'date',
        }),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''


class AddTransactionStorage(forms.Form):
    form_name = 'Добавление транзакции'
    button_text = 'Добавить'

    title = forms.CharField(
        label='',
        max_length=63,
        min_length=4,
        widget=forms.TextInput(attrs={
            'placeholder': 'Название',
            'autofocus': True,
        }),
    )
    description = forms.CharField(
        label='',
        max_length=1023,
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Описание',
            'rows': 10,
        }),
    )
    date = forms.DateField(
        label='',
        initial=datetime.date.today().strftime("%Y-%m-%d"),
        widget=forms.DateInput(attrs={
            'type': 'date',
        }),
    )
    is_repeated = forms.BooleanField(
        label='Повторяется',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'input-checkbox',
        }),
    )
    frequency = forms.IntegerField(
        label='дней',
        required=False,
        min_value=0,
        max_value=365,
        initial=30,
    )

    value = forms.FloatField(
        label='₽',
        initial="1000.00",
    )
    is_confirmed = forms.BooleanField(
        label='Всегда подтверждено',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'input-checkbox',
        }),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''


class AddTransaction(forms.ModelForm):
    form_name = 'Редактирование транзакции'
    button_text = 'Редактировать'

    data = []

    execution_date = forms.DateField(
        label='',
        initial=datetime.date.today().strftime("%Y-%m-%d"),
        widget=forms.DateInput(attrs={
            'type': 'date',
        }),
    )

    value = forms.FloatField(
        label='₽',
        initial="1000.00",
    )

    is_confirmed = forms.BooleanField(
        label='Подтверждена',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'input-checkbox',
        }),
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''

    class Meta:
        model = Transaction
        exclude = ('storage', 'storage_order_number', 'created_datetime',)


class AddTarget(forms.Form):
    form_name = 'Добавление цели'
    button_text = 'Добавить'

    title = forms.CharField(
        label='',
        max_length=63,
        min_length=4,
        widget=forms.TextInput(attrs={
            'placeholder': 'Название',
            'autofocus': True,
        }),
    )
    description = forms.CharField(
        label='',
        max_length=1023,
        required=False,
        widget=forms.Textarea(attrs={
            'placeholder': 'Описание',
            'rows': 10,
        }),
    )
    date = forms.DateField(
        label='',
        initial=datetime.date.today().strftime("%Y-%m-%d"),
        widget=forms.DateInput(attrs={
            'type': 'date',
        }),
    )
    has_time = forms.BooleanField(
        label='Добавить время',
        required=False,
        widget=forms.CheckboxInput(attrs={
            'class': 'input-checkbox',
        }),
    )
    time = forms.TimeField(
        label='',
        initial="12:00",
        widget=forms.TimeInput(attrs={
            'type': 'time'}),
    )
    value = forms.FloatField(
        label='₽',
        min_value=0,
        initial="1000.00",
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = ''
