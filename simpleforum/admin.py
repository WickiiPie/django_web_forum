from django.contrib import admin

# Register your models here.
from .models import Forum, SubForum, Thread, Post, UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'address')


class ThreadAdmin(admin.ModelAdmin):

    search_fields = ('title', 'created_at')
    list_display = ('title', 'user_id', 'sub_forum_id', 'updated_at')

class SubForumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Forum)
admin.site.register(SubForum, SubForumAdmin)
admin.site.register(Thread, ThreadAdmin)
admin.site.register(Post)
admin.site.register(UserProfile, UserProfileAdmin)
