from django.http import *
from django.shortcuts import render

from .forms import AddTarget
from .backends import add_target, get_targets


def add_target_page(request):
    if request.method == 'POST':
        form = AddTarget(request.POST)
        if form.is_valid():
            form = add_target(form)
            if not form.errors:
                return HttpResponseRedirect('/home')
    else:
        form = AddTarget()
    return render(request, 'add.html', {'form': form})


def get_targets_page(request):
    if request.method == 'POST':
        return HttpResponseBadRequest()
    else:
        targets = get_targets()
    return render(request, 'get_targets.html', {'targets': targets})
