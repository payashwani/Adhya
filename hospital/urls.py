from django.urls import path
from django.http import HttpResponse

def test(request):
    return HttpResponse("This app is connected!")

urlpatterns = [
    path('', test),
]
