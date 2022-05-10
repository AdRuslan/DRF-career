from django.contrib import admin
from .models import Employer, Finder, Vacancy
from simple_history.admin import SimpleHistoryAdmin


admin.site.register(Finder, SimpleHistoryAdmin)
admin.site.register(Employer, SimpleHistoryAdmin)
admin.site.register(Vacancy, SimpleHistoryAdmin)
