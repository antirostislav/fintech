from django.http import HttpResponseRedirect
from django.shortcuts import render
from .backends import login_user, register_user
from .forms import RegisterForm, LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form = login_user(request, form)
            if not form.errors:
                return HttpResponseRedirect('/home')
    else:
        form = LoginForm()
    return render(request, 'authentication.html', {'form': form})


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form = register_user(form)
            if not form.errors:
                return HttpResponseRedirect('/authentication/login')
    else:
        form = RegisterForm()
    return render(request, 'authentication.html', {'form': form})
