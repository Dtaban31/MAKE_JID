from django.db import models
from django.contrib.auth.models import AbstractUser

# Your custom Account model
class Account(AbstractUser):
    # You can add custom fields here if you want
    # Example: bio = models.TextField(blank=True)
    pass

class Post(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    event_date = models.DateTimeField()
    created_by = models.ForeignKey(Account, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class RSVP(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} RSVP'd to {self.post.title}"
