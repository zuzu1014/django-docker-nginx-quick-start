from django.conf import settings
from django.shortcuts import redirect
from django.contrib import messages
from .models import *
from django.http import HttpResponse

# 로그인 확인


def login_required(function):
    def wrap(request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('/login')
        return function(request, *args, **kwargs)
    return wrap

def logout_required(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')
        return function(request, *args, **kwargs)
    return wrap
