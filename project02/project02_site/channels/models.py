from django.db import models
from django.contrib.auth.models import User

class Channel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    subscriber_count = models.IntegerField(default=0)
    banner = models.ImageField(upload_to='banners/', blank=True, default='placeholder.png')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name