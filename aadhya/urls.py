"""
URL configuration for aadhya project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to Aadhya Backend</h1>")

urlpatterns = [
    path('', home),  # test homepage
    path('admin/', admin.site.urls),

    path('guidance/', include('guidance.urls')),
    path('chatbot/', include('chatbot.urls')),
    path('health/', include('health.urls')),
    path('panic/', include('panic.urls')),
    path('hospital/', include('hospital.urls')),
    path('newborn/', include('newborn.urls')),
    path('forum/', include('forum.urls')),
    path('schemes/', include('schemes.urls')),
]

