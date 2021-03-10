from django.urls import path
from . import views

app_name = 'accounts'


urlpatterns = [
    path('', views.index),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.logout),
    path('register/', views.RegisterView.as_view()),
    path('mypage/', views.MypageView.as_view()),
    path('password-change/', views.PasswordChangeView.as_view(), name="password-change"),
    path('delete-account/', views.DeleteView.as_view()),
    #ajax
    path('check_unique_id/',views.check_unique_id, name='check_unique_id')
]
