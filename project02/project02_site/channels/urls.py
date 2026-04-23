from django.urls import path
from .views import (
    ChannelListView, 
    ChannelDetailView, 
    ChannelCreateView,
    ChannelUpdateView,
    ChannelDeleteView,          
)

urlpatterns = [
    path('', ChannelListView.as_view(), name='channel_list'),
    path('<int:pk>/', ChannelDetailView.as_view(), name='channel_detail'),
    path('add/', ChannelCreateView.as_view(), name='channel_add'),
    path('<int:pk>/edit/', ChannelUpdateView.as_view(), name='channel_edit'),
    path('<int:pk>/delete/', ChannelDeleteView.as_view(), name='channel_delete'),  ]
