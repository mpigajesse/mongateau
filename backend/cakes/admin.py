from django.contrib import admin
from .models import CakeType


@admin.register(CakeType)
class CakeTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'cake_type', 'base_price', 'is_available', 'created_at']
    list_filter = ['is_available', 'cake_type']
    search_fields = ['name', 'description']
    list_editable = ['is_available']
    readonly_fields = ['created_at', 'updated_at']
