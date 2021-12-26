from django import forms

class AddTarget(forms.Form):
    form_name = 'Добавление цели'
    button_text = 'Добавить'

    title = forms.CharField(
        label='Название',
        max_length=63,

        min_length=4,
        widget=forms.TextInput(attrs={'autofocus': True}),
    )
    description = forms.CharField(
        label='Описание',
        max_length=1023,
        widget=forms.Textarea(attrs={'rows':10}),
    )
    datetime = forms.DateTimeField(
        label='Дата',
        widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}),
    )
    value = forms.FloatField(
        min_value=0,
        initial=1000.00,
        label='Сумма',
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
