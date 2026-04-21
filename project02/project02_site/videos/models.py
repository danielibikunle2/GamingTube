from django.db import models
from channels.models import Channel
from games.models import Game

class Video(models.Model):
    title = models.CharField(max_length=200)
    thumbnail = models.ImageField(upload_to='thumbnails/', blank=True, default='placeholder.png')
    views = models.IntegerField(default=0)
    upload_date = models.DateField()
    channel = models.ForeignKey(Channel, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True, blank=True)
    youtube_url = models.URLField(blank=True)

    def __str__(self):
        return self.title
