"""voyage URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.http import JsonResponse
from django.urls import path, include
from django.contrib import admin

def home(request):
    return JsonResponse({"message": "Welcome to the Voyage API!"})

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('profiles.urls')),  # Include your app's API URLs
    path('', home),  # Redirect `/` to a JSON response
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('profiles.urls')),
    path('api/', include('posts.urls')),  
    path('api/', include("comments.urls")),
    path('api/', include('likes.urls')), 
    path('api/', include('followers.urls')),
    
]
