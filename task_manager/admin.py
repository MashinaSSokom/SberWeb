from django.contrib import admin
from . import models


@admin.register(models.Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ('lastname', 'firstname', 'department_code', 'post',)
    search_fields = ('lastname', 'firstname', 'department_code', 'post',)


@admin.register(models.Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'creator', 'date_start',)
    search_fields = ('title', 'creator', 'date_start',)
