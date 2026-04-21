from django.shortcuts import render, get_object_or_404, redirect
from .models import Review
from .forms import ReviewForm
from channels.models import Channel

def add_review(request, channel_pk):
    channel = get_object_or_404(Channel, pk=channel_pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.channel = channel
            review.user = request.user
            review.save()
            return redirect('channel_detail', pk=channel_pk)
    else:
        form = ReviewForm()
    context = {'form': form, 'channel': channel}
    return render(request, 'reviews/add_review.html', context)
