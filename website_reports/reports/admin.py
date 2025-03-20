from django.contrib import admin
from .models import Report

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('url', 'status_code', 'date_reported', 'date_retrieved', 'is_malicious')
    search_fields = ('url',)
