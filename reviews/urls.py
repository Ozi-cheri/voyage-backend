from django.urls import path
from .views import ReviewListCreateView, ReviewModerateView, ReviewDetail

urlpatterns = [
    path("posts/<int:post_id>/reviews/", ReviewListCreateView.as_view(), name="reviews-list-create"),
    path("reviews/<int:pk>/moderate/", ReviewModerateView.as_view(), name="reviews-moderate"),
    path("reviews/<int:pk>/", ReviewDetail.as_view(), name="review-detail"),  
]
