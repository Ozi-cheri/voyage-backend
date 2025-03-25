from django.shortcuts import get_object_or_404
from rest_framework import generics, permissions
from .models import Review
from .serializers import ReviewSerializer
from posts.models import Post  # Import Post model
from profiles.permissions import IsOwnerOrReadOnly


class ReviewListCreateView(generics.ListCreateAPIView):
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        """
        Returns reviews related to a specific post.
        """
        post_id = self.kwargs.get('post_id')  # Get post ID from URL
        return Review.objects.filter(post_id=post_id)  # Filter by post_id

    def perform_create(self, serializer):
        """
        Associates the review with the authenticated user and the specified post.
        """
        post_id = self.kwargs.get('post_id')
        post = get_object_or_404(Post, id=post_id)  # Get the post
        serializer.save(user=self.request.user, post=post)  # Save with user & post


class ReviewModerateView(generics.DestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAdminUser]  # Only admins


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
