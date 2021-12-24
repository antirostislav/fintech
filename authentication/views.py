from django.http import HttpResponseRedirect
from django.shortcuts import render
from .backends import login, register
from .forms import RegisterForm, LoginForm


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form = login(request, form)
            if not form.errors:
                return HttpResponseRedirect('/home')
    else:
        form = LoginForm()
    return render(request, 'authentication.html', {'form': form})


def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form = register(form)
            if not form.errors:
                return HttpResponseRedirect('/authentication/login')
    else:
        form = RegisterForm()
    return render(request, 'authentication.html', {'form': form})
