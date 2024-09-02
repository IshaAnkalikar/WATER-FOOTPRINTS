# calculator/admin.py

from django.contrib import admin
from .models import WaterUsage

class WaterUsageAdmin(admin.ModelAdmin):
    list_display = ('num_people', 'total_usage')
    list_filter = ('num_people',)

admin.site.register(WaterUsage, WaterUsageAdmin)
