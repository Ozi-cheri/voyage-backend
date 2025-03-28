from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer
from posts.models import Post  
from profiles.permissions import IsOwnerOrReadOnly


class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        
        post_id = self.kwargs.get('post_id')  
        return Review.objects.filter(post_id=post_id)  

    def perform_create(self, serializer):
        
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)  
        serializer.save(user=self.request.user, post=post)  


class ReviewModerateView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAdminUser]  


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
