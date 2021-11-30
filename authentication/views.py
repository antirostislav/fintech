from django.shortcuts import render
from django.urls import path


def home_page(request):
    return render(request=request, template_name='home.html', context={'user': request.user})
