from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponseBadRequest
from django.shortcuts import render

from authentication.models import User
from .forms import AddTarget
from .backends import add_target, get_targets


@login_required
def add_target_page(request):
    if request.method == 'POST':
        form = AddTarget(request.POST)
        if form.is_valid():
            add_target(owner=request.user, **form.cleaned_data)
            return HttpResponseRedirect('/finance/home?' + request.GET.urlencode())
    else:
        form = AddTarget()
    return render(request, 'finance/add_target.html', {'form': form})


@login_required
def get_targets_page(request):
    if request.method == 'POST':
        return HttpResponseBadRequest()
    else:
        targets = get_targets(owner=request.user)
    return render(request, 'finance/get_targets.html', {'targets': targets})
