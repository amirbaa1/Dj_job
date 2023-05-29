from django.contrib import admin
from .models import Company, Job


@admin.register(Company)
class AdminCompany(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'name_partners']
    list_filter = ['name_partners']


@admin.register(Job)
class AdminJob(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']
