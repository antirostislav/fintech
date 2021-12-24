from django import forms


class RegisterForm(forms.Form):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=255,
        min_length=4,
        widget=forms.TextInput(attrs={'autofocus': True}))
    email = forms.EmailField(
        label='Электронная почта',
        max_length=255,
        min_length=4)
    password = forms.CharField(
        label='Пароль',
        max_length=255,
        min_length=8,
        strip=False,
        widget=forms.PasswordInput(),
    )

    class Meta:
        form_name = 'Регистрация'
        button_text = 'Зарегистрироваться'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class LoginForm(forms.Form):
    username = forms.CharField(
        label='Имя пользователя',
        max_length=255,
        min_length=4,
        widget=forms.TextInput(attrs={'autofocus': True}))
    password = forms.CharField(
        label='Пароль',
        max_length=255,
        min_length=8,
        strip=False,
        widget=forms.PasswordInput())

    class Meta:
        form_name = 'Вход'
        button_text = 'Войти'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
