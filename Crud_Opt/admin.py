from django.contrib import admin
from .models import Plan

class MyPlanAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'place', 'phone', 'email', 'created_at', 'update_at']

admin.site.register(Plan, MyPlanAdmin)