from django.shortcuts import render, get_object_or_404, redirect
from .models import Video
from .forms import VideoForm

def video_list(request):
    videos = Video.objects.all()
    context = {'videos': videos}
    return render(request, 'videos/video_list.html', context)

def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    context = {'video': video}
    return render(request, 'videos/video_detail.html', context)

def video_add(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video_list')
    else:
        form = VideoForm()
    context = {'form': form}
    return render(request, 'videos/video_add.html', context)