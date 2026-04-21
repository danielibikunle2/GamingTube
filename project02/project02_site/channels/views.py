from django.shortcuts import render, get_object_or_404, redirect
from .models import Channel
from .forms import ChannelForm
from django.views.generic import ListView, DetailView
from .models import Channel

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

def channel_add(request):
    if request.method == 'POST':
        form = ChannelForm(request.POST, request.FILES)
        if form.is_valid():
            channel = form.save(commit=False)
            channel.owner = request.user
            channel.save()
            form.save_m2m()  
            return redirect('channel_list')
    else:
        form = ChannelForm()
    context = {'form': form}
    return render(request, 'channels/channel_add.html', context)