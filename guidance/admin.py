# Register your models here.
from django.contrib import admin
from .models import Video, AudioGuide

admin.site.register(Video)
admin.site.register(AudioGuide)
