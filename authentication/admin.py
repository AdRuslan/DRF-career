from django.contrib import admin
from django.contrib.auth.models import Group
from .models import User
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(User, SimpleHistoryAdmin)
admin.site.unregister(Group)
