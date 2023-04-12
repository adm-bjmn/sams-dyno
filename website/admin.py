from django.contrib import admin
from .models import BlogPost, Topic

# Register your models here.
admin.site.register(Topic)
admin.site.register(BlogPost)
