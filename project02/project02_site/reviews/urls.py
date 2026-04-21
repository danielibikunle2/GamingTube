from django.urls import path
from . import views

urlpatterns = [
    path('add/<int:channel_pk>/', views.add_review, name='add_review'),
]