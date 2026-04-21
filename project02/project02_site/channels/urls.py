from django.urls import path
from .views import ChannelListView, ChannelDetailView, ChannelCreateView

urlpatterns = [
    path('', ChannelListView.as_view(), name='channel_list'),
    path('<int:pk>/', ChannelDetailView.as_view(), name='channel_detail'),
    path('add/', ChannelCreateView.as_view(), name='channel_add'),
]