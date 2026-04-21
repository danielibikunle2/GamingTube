from django.urls import path
from .views import ChannelListView, ChannelDetailView, channel_add 
urlpatterns = [
    path('', ChannelListView.as_view(), name='channel_list'),
    path('<int:pk>/', ChannelDetailView.as_view(), name='channel_detail'),
    path('add/', channel_add, name='channel_add'),                 
]