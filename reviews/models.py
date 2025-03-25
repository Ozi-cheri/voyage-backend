from django.db import models
from django.contrib.auth.models import User
from posts.models import Post 

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # The user who created the review
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  # The post being reviewed
    rating = models.IntegerField()  # Rating for the post (1-5)
    comment = models.TextField()  # The review comment
    moderated = models.BooleanField(default=False)  # Whether the review has been approved or not
    created_at = models.DateTimeField(auto_now_add=True)  # Time the review was created

    def __str__(self):
        return f'Review by {self.user} on {self.post.title} - Rating: {self.rating}/5'
