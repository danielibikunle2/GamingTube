from django.urls import path
from . import views

urlpatterns = [
    path('', views.channel_list, name='channel_list'),
    path('<int:pk>/', views.channel_detail, name='channel_detail'),
    path('add/', views.channel_add, name='channel_add'),
]