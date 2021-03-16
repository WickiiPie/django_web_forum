from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify
# Create your models here.
class Forum(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(default="no description")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def get_absolute_url(self):
    #     return reverse('Forum.views.forum_list_view', args=[str(self.id)])

    def get_absolute_url(self):
        return reverse("simpleforum:sub_forum_list_view", args=[str(self.id)])
        # return reverse("simpleforum:forum_list_view")

    # def __str__(self):
    #     return self.name


class SubForum(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(default="no description")
    forum_id = models.ForeignKey('simpleforum.forum', on_delete=models.CASCADE,
                                 null=True)
    slug = models.SlugField(null=True, unique=True)

    def get_absolute_url(self):
        return reverse("simpleforum:thread_list_view", args=[str(self.slug)])

    def __str__(self):
        return self.name


class ThreadManager(models.Manager):
    def get_queryset(self):
        return super(ThreadManager, self).get_queryset().filter(sub_forum_id=1)


class Thread(models.Model):
    objects = models.Manager()  # default manager
    # published = models.Manager()     # for using custom ORM, use published instead of objects #example thread.published.all()
    published = ThreadManager()     # using subclass to use specific manager
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100, null=False, unique=True)
    content = models.CharField(max_length=100, null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sub_forum_id = models.ForeignKey('simpleforum.SubForum',
                                     on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    thread_id = models.ForeignKey(
        'simpleforum.thread', on_delete=models.CASCADE, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    parent_id = models.ForeignKey(
        'simpleforum.post', on_delete=models.CASCADE, null=True, blank=True,
        related_name="parent")

    class Meta:
        ordering = ['created_at']

    def get_absolute_url(self):
        return reverse("simpleforum:thread_details_view", kwargs={"id": self.id})

    # def __str__(self):
    #     return '{}-{}'.format(self.thread_id.title, str(self.user_id.username))


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                related_name='profile')  # 1:1 with auth user
    dob = models.DateField(null=True, blank=True)
    # photo = models.ImageField(null=True, blank=True) # requires pip install pillow
    address = models.CharField(max_length=100)

    def __str__(self):
        return "Profile of user {}".format(self.user.username)
