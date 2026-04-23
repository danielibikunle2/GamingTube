from django.shortcuts import render, get_object_or_404, redirect
from .models import Channel
from .forms import ChannelForm
from django.views.generic import ListView, DetailView, CreateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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


class ChannelCreateView(LoginRequiredMixin, CreateView):
    model = Channel
    form_class = ChannelForm
    template_name = 'channels/channel_add.html'
    success_url = reverse_lazy('channel_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user 
        return super().form_valid(form)
    
class ChannelDeleteView(LoginRequiredMixin, DeleteView):
    model = Channel
    template_name = 'channels/channel_confirm_delete.html'
    success_url = reverse_lazy('channel_list')

    def get_queryset(self):
        return super().get_queryset().filter(owner=self.request.user)