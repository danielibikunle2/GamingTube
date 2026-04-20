from django.shortcuts import render, get_object_or_404, redirect
from .models import Channel
from .forms import ChannelForm


def channel_list(request):
    channels = Channel.objects.all()
    context = {'channels': channels}
    return render(request, 'channels/channel_list.html', context)

def channel_detail(request, pk):
    channel = get_object_or_404(Channel, pk=pk)
    context = {'channel': channel}
    return render(request, 'channels/channel_detail.html', context)

def channel_add(request):
    if request.method == 'POST':
        form = ChannelForm(request.POST, request.FILES)
        if form.is_valid():
            channel = form.save(commit=False)
            channel.owner = request.user
            channel.save()
            form.save_m2m()  # needed to save ManyToMany fields
            return redirect('channel_list')
    else:
        form = ChannelForm()
    context = {'form': form}
    return render(request, 'channels/channel_add.html', context)