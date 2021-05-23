from django.contrib import admin
from . import models


@admin.register(models.CustomUser)
class CustomUser(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name', 'division_code_gosb', 'division_code_vsp', 'post',)
