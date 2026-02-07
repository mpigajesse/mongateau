from django.contrib import admin
from .models import Order, CustomCakeRequest


@admin.register(CustomCakeRequest)
class CustomCakeRequestAdmin(admin.ModelAdmin):
    list_display = [
        'request_number',
        'customer_name',
        'customer_phone',
        'delivery_date',
        'status',
        'estimated_budget',
        'created_at',
    ]
    list_filter = ['status', 'delivery_date', 'created_at']
    search_fields = ['request_number', 'customer_name', 'customer_phone']
    readonly_fields = ['request_number', 'created_at', 'updated_at']
    list_editable = ['status']

    fieldsets = (
        ('Informations de demande', {
            'fields': ('request_number', 'status')
        }),
        ('Informations client', {
            'fields': ('customer_name', 'customer_phone')
        }),
        ('Détails', {
            'fields': ('delivery_date', 'custom_message', 'estimated_budget')
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = [
        'order_number',
        'customer_name',
        'customer_phone',
        'cake_type',
        'delivery_date',
        'status',
        'total_price',
        'created_at'
    ]
    list_filter = ['status', 'delivery_date', 'created_at', 'cake_type']
    search_fields = ['order_number', 'customer_name', 'customer_phone']
    readonly_fields = ['order_number', 'created_at', 'updated_at', 'ticket_path']
    list_editable = ['status']
    
    fieldsets = (
        ('Informations de commande', {
            'fields': ('order_number', 'status')
        }),
        ('Informations client', {
            'fields': ('customer_name', 'customer_phone')
        }),
        ('Détails du gâteau', {
            'fields': ('cake_type', 'custom_message', 'total_price')
        }),
        ('Livraison', {
            'fields': ('delivery_date', 'delivery_address')
        }),
        ('Ticket', {
            'fields': ('ticket_path',)
        }),
        ('Dates', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
