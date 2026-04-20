from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Game(models.Model):
    title = models.CharField(max_length=200)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)
    cover_image = models.ImageField(upload_to='games/', blank=True, default='placeholder.png')
    release_year = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title