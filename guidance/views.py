from django.http import JsonResponse
from .models import Video, AudioGuide

def video_list(request):
    videos = list(Video.objects.values())
    return JsonResponse({"videos": videos})

def audio_list(request):
    audios = list(AudioGuide.objects.values())
    return JsonResponse({"audios": audios})
