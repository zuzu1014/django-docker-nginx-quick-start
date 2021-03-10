from django.urls import path
from . import views

app_name = 'posts'


urlpatterns = [
    path('posts/<str:section>/', views.posts),
]
