from django.db import models
from django.utils import timezone
from users.models import User

# Post Model
class Post(models.Model):
    post_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # A user can have many posts
    post_content = models.TextField()
    post_image_url = models.URLField(blank=True, null=True)
    post_like_count = models.IntegerField(default=0)
    
    # Many-to-Many relationship to track users who liked the post
    post_liked_by = models.ManyToManyField(User, related_name='liked_posts', blank=True)
    post_disliked_by = models.ManyToManyField(User, related_name='dis_liked_posts', blank=True)

    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Post by {self.user.user_username} on {self.created_at}"


# Comment Model
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')  # Many comments to one post
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_who_made')  # Many comments by one user
    comment_content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.user.user_username} on {self.created_at}"

