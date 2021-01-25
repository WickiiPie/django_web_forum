from django.contrib import admin

# Register your models here.
from .models import forum, sub_forum

admin.site.register(forum)
admin.site.register(sub_forum)


