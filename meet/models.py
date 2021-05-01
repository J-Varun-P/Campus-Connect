from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.TextField(default='Say Something about yourself!')

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="activities")
    title = models.CharField(max_length=128)
    description = models.TextField()
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title} by {self.user.username} at {self.time}"

class Joining(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="joined_activities")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="user_activities")

    def __str__(self):
        return f"{self.user.username} joined {self.activity.title}"

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="commented_activities")
    comment = models.TextField()

    def __str__(self):
        return f"{self.user.username} commented on {self.activity.title}"

class Deleted(models.Model):
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE, related_name="deleted_activities")

    def __str__(self):
        return f"{self.activity.user.username} deleted {self.activity}"
