from django.http import *
from django.shortcuts import render


def landing(request):
    if request.method == "POST":
        return HttpResponseBadRequest(405)
    else:
        return render(request, 'landing/landing.html', {'user': request.user})
