from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from .models import *
from django.utils.decorators import method_decorator


def posts(request, section):
    
    posts = Post.objects.all()

    return render(request, 'posts/index.html', {"posts": posts})
