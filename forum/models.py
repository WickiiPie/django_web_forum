from django.db import models
from django.shortcuts import reverse

from django.contrib.auth.models import User
# Create your models here.
class forum(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    description = models.TextField(default="no description")

    # def get_absolute_url(self):
    #     return reverse('forum.views.forum_list_view', args=[str(self.id)])
    def get_absolute_url(self):
        return reverse("forum:sub_forum_list_view", args=[str(self.id)])
        # return reverse("forum:forum_list_view")

    def __str__(self):
        return self.name

class sub_forum(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(default="no description")
    forum_id = models.ForeignKey('forum.forum', on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return reverse("forum:thread_list_view", args=[str(self.id)])


class ThreadManager(models.Manager):
    def get_queryset(self):
        return super(ThreadManager, self).get_queryset().filter(sub_forum_id=1)

class thread(models.Model):

    objects = models.Manager() # default manager

    # published = models.Manager()     # for using custom ORM, use published instead of objects #example thread.published.all()

    published = ThreadManager()     # using subclass to use specific manager

    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=False, unique=True)
    content = models.CharField(max_length=100, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sub_forum_id = models.ForeignKey('forum.sub_forum', on_delete=models.CASCADE, null=True)


    class Meta:
        ordering = ['-created_at']
    def __str__(self):
        return self.title

class post(models.Model):
    id = models.AutoField(primary_key=True)
    thread_id = models.ForeignKey('forum.thread', on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_id = models.ForeignKey('forum.post', on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("forum:thread_details_view", kwargs={"id":self.id})

    # def __str__(self):
    #     return '{}-{}'.format(self.thread.title, str(self.user.username))

class user_profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # one to one with auth user
    dob = models.DateField(null=True, blank = True)
    # photo = models.ImageField(null=True, blank=True) # requires pip install pillow
    address = models.CharField(max_length=100 )

    def __str__(self):
        return "Profile of user {}".format(self.user.username)