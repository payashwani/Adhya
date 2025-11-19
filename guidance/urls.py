from django.urls import path
from . import views

urlpatterns = [
    path('videos/', views.video_list, name='video_list'),
    path('audios/', views.audio_list, name='audio_list'),
]
