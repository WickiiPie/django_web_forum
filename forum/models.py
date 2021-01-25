from django.db import models
from django.shortcuts import reverse

# Create your models here.
class forum(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default="no description")

    def get_absolute_url(self):
        return reverse('forum.views.forum_list_view', args=[str(self.id)])


class sub_forum(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(default="no description")
    forum_id = models.ForeignKey('forum.forum', on_delete=models.CASCADE, null=True)
