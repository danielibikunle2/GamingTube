from django.urls import path
from .views import VideoListView, VideoDetailView, VideoCreateView

urlpatterns = [
    path('', VideoListView.as_view(), name='video_list'),
    path('<int:pk>/', VideoDetailView.as_view(), name='video_detail'),
    path('add/', VideoCreateView.as_view(), name='video_add'),
]