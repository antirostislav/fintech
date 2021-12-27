from django import forms
from django.contrib.auth import password_validation, authenticate
from django.contrib.auth import login as login_user
from django.core.exceptions import ValidationError

from .models import User


def register(form: forms.Form) -> forms.Form:
    data = form.clean()

    try:
        password_validation.validate_password(data['password'], User)
    except ValidationError as error:
        form.add_error('password', error)

    if not form.errors:
        user = User.objects.create_user(**data)
        user.set_password(data['password'])
        user.save()
    return form


def login(request, form: forms.Form) -> forms.Form:
    user = authenticate(request, **form.cleaned_data)
    if user is not None:
        login_user(request, user)
    else:
        form.add_error('username', 'Имя и/или пароль неверны')
    return form
