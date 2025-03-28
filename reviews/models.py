from django.db import models
from django.contrib.auth.models import User
from posts.models import Post 

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    post = models.ForeignKey(Post, on_delete=models.CASCADE)  
    rating = models.IntegerField()  
    comment = models.TextField()  # 
    moderated = models.BooleanField(default=False)  
    created_at = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f'Review by {self.user} on {self.post.title} - Rating: {self.rating}/5'
