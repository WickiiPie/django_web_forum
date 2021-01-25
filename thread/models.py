from django.db import models

from django.contrib.auth.models import User


# Create your models here.
class thread(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=False, unique=True)
    content = models.CharField(max_length=100, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    sub_forum_id = models.ForeignKey('forum.sub_forum', on_delete=models.CASCADE, null=True)

class post(models.Model):
    id = models.AutoField(primary_key=True)
    thread_id = models.ForeignKey('thread.thread', on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    parent_id = models.ForeignKey('thread.post', on_delete=models.CASCADE, null=True)

