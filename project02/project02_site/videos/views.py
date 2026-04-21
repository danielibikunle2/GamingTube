from django.shortcuts import render, get_object_or_404, redirect
from .forms import VideoForm
from django.views.generic import ListView, DetailView, CreateView
from .models import Video
from django.urls import reverse_lazy
class VideoListView(ListView):
    model = Video
    template_name = 'videos/video_list.html'
    context_object_name = 'videos'
    ordering = ['-upload_date']          

class VideoDetailView(DetailView):
    model = Video
    template_name = 'videos/video_detail.html'
    context_object_name = 'video'
    pk_url_kwarg = 'pk'

class VideoCreateView(CreateView):
    model = Video
    form_class = VideoForm
    template_name = 'videos/video_add.html'
    success_url = reverse_lazy('video_list')