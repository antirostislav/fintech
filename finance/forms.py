import datetime

from django import forms


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
