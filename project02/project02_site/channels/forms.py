from django import forms
from .models import Channel
from games.models import Game

class ChannelForm(forms.ModelForm):
    games = forms.ModelMultipleChoiceField(
        queryset=Game.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Channel
        fields = ['name', 'description', 'subscriber_count', 'banner', 'games']