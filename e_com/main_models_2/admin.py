from django.contrib import admin
from .models import Item, Order, Client


class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count']
    list_filter = ['count']
    search_fields = ['name', 'description']
    search_help_text = 'Поиск по названию и описанию'
    readonly_fields = ['date_of_edit']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id_client', 'total_sum', 'date_of_creation']
    ordering = ['-date_of_creation']
    list_filter = ['total_sum']
    readonly_fields = ['date_of_creation']


class ClientAdmin(admin.ModelAdmin):
    readonly_fields = ['date_of_registration']
    fieldsets = [
        (
            None,
            {
                'classes': ['wide'],
                'fields': ['name', 'email'],
            }
        ),
        (
            'Подробности',
            {
                'classes': ['collapse'],
                'description': 'Полная информация о пользователе',
                'fields': ['phone_number', 'address', 'date_of_registration'],
            },
        ),
    ]


admin.site.register(Item, ItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Client, ClientAdmin)
