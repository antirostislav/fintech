from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render
from .backends import login, register, logout
from .forms import RegisterForm, LoginForm


def login_page(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            form = login(request, form)
            if not form.errors:
                if not form.errors:
                    if request.GET.__contains__('next'):
                        get_params = request.GET.copy()
                        return HttpResponseRedirect(get_params.pop('next')[0] + '?' + get_params.urlencode())
                    else:
                        return HttpResponseRedirect('/home?' + request.GET.urlencode())
    else:
        form = LoginForm()
    return render(request, 'authentication/authentication.html', {'form': form})


def register_page(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form = register(form)
            if not form.errors:
                return HttpResponseRedirect('/authentication/login?' + request.GET.urlencode())
    else:
        form = RegisterForm()
    return render(request, 'authentication/authentication.html', {'form': form})


def logout_page(request):
    if request.method == 'POST':
        return HttpResponseBadRequest()
    else:
        logout(request)
        return HttpResponseRedirect('/')

