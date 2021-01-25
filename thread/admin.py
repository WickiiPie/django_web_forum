from django.contrib import admin


from .models import thread, post

# Register your models here.
admin.site.register(thread)
admin.site.register(post)