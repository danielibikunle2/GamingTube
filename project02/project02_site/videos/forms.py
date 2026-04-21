from django import forms
from .models import Video

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'thumbnail', 'views', 'upload_date', 'channel', 'game', 'youtube_url']
        widgets = {
            'upload_date': forms.DateInput(attrs={'type': 'date'}),
        }