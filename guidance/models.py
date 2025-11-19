# Create your models here.
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    youtube_url = models.URLField()
    category = models.CharField(max_length=100, default="General")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class AudioGuide(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    audio_file = models.FileField(upload_to='audio_guides/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
