from django.contrib import admin
from .models import Warehouse, ItemType, ItemInstance,ItemCategory

admin.site.register(Warehouse)
admin.site.register(ItemType)
admin.site.register(ItemInstance)
admin.site.register(ItemCategory)