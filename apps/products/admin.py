from django.contrib import admin
from .models import ProductsModel

@admin.register(ProductsModel)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'sku', 'status', 'is_active',)
    search_fields = ('name',)
    list_filter = ('status', 'is_active')
