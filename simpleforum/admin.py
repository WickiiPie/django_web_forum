from django.contrib import admin

# Register your models here.
from simpleforum.models import Forum, SubForum, Thread, Post, UserProfile

class SubForumAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)
    prepopulated_fields = {'slug': ('name',), }


admin.site.register(Forum)
admin.site.register(SubForum, SubForumAdmin)

admin.site.register(Thread)
admin.site.register(Post)
admin.site.register(UserProfile)
