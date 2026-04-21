from django.shortcuts import render, get_object_or_404, redirect
from .models import Channel
from .forms import ChannelForm
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy

class ChannelListView(ListView):
    model = Channel
    template_name = 'channels/channel_list.html'
    context_object_name = 'channels'
    ordering = ['name']                

class ChannelDetailView(DetailView):
    model = Channel
    template_name = 'channels/channel_detail.html'
    context_object_name = 'channel'
    pk_url_kwarg = 'pk'

class ChannelCreateView(CreateView):
    model = Channel
    form_class = ChannelForm
    template_name = 'channels/channel_add.html'
    success_url = reverse_lazy('channel_list')