from django.contrib import admin

# Register your models here.
# Register your models here.
from .models import forum, sub_forum, thread, post, user_profile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'address')

admin.site.register(forum)
admin.site.register(sub_forum)
admin.site.register(thread)
admin.site.register(post)
admin.site.register(user_profile, UserProfileAdmin)