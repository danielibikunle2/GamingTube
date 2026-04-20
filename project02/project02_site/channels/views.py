from django.shortcuts import render, get_object_or_404
from .models import Channel

def channel_list(request):
    channels = Channel.objects.all()
    context = {'channels': channels}
    return render(request, 'channels/channel_list.html', context)

def channel_detail(request, pk):
    channel = get_object_or_404(Channel, pk=pk)
    context = {'channel': channel}
    return render(request, 'channels/channel_detail.html', context)