from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import forum, sub_forum, thread, post, user_profile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'address')

class ThreadAdmin(admin.ModelAdmin):

    search_fields = ('title', 'created_at')
    list_display = ('title', 'user_id', 'sub_forum_id', 'updated_at')

admin.site.register(forum)
admin.site.register(sub_forum)
admin.site.register(thread, ThreadAdmin)
admin.site.register(post)
admin.site.register(user_profile, UserProfileAdmin)