from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
# unregister Groups - Not needed
admin.site.unregister(Group)
