from django.contrib import admin

from src.items.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass
