from django.urls import path
from . import views

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('<int:pk>/', views.video_detail, name='video_detail'),
    path('add/', views.video_add, name='video_add'),
]