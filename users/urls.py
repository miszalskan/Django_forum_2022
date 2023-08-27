from . import views
from django.urls import path
from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('login/', views.login_user, name='login'),
    path('register/', views.register_user, name='register'),
    path('logout/', views.logout_user, name='logout'),
    path('confirm_password/', views.confirm, name='confirm'),
    path('send_email/', views.send_email, name='sendemail'),
    path('profile/<int:pk>', views.user_profile, name='user_profile'),
    path('forget_password/', views.forget_password, name="forget_password"),
    path('change_password/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',
         views.change_password, name='change_password'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', activate,
         name='activate'),
]
