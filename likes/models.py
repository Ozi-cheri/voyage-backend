from django.db import models
from django.contrib.auth.models import User
from posts.models import Post  

# Create your models here.
class Like(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("owner", "post")  # Prevent duplicate likes from the same user

    def __str__(self):
        return f"{self.owner} liked {self.post}"
