from django.db import models
from django.contrib.auth.models import User
from news.models import News
# Create your models here.


# class CustomerUser(AbstractUser):
#     adress = models.CharField(max_length=200, blank=True, null=True)
#     image = models.ImageField(upload_to='users/', default='users/images.png')
#
#
#     def __str__(self):
#         return self.username

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(News, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    like = models.PositiveIntegerField(default=0)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"
