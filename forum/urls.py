from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('add_post/', views.add_post, name='add_post'),
    path('post/<str:pk>', views.post_detail, name='post_detail'),
    path('about/', views.about, name='about'),
    path('post/<str:pk>/add_comment/', views.add_comment, name="add_comment"),
]
