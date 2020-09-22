from django.contrib import admin
from .models import Product, Category, Condition, Sale

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
        'condition',
        'sale',
    )

    ordering = ('sku',)

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class ConditionAdmin(admin.ModelAdmin):
    list_display = (
        'condition',
    )

class SaleAdmin(admin.ModelAdmin):
    list_display = (
        'sale',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Condition, ConditionAdmin)
admin.site.register(Sale, SaleAdmin)