from django.contrib import admin
from django.contrib.auth.models import Group
from .models import UserAbstract

admin.site.unregister(Group)
admin.site.register(UserAbstract)