from django.urls import path
from .views import ProfileListCreateAPIView, ProfileDetailAPIView

urlpatterns = [
    path('profiles/', ProfileListCreateAPIView.as_view(), name='profile-list-create'),
    path('profiles/<int:pk>/', ProfileDetailAPIView.as_view(), name='profile-detail'),
     
]
