from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_at']
    list_filter = ['created_at']
    search_fields = ['title']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['title']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'short_desc', 'discount', 'size', 'sku', 'description', 'category', 'tag']
    search_fields = ['title']

@admin.register(Characteristic)
class CharacteristicAdmin(admin.ModelAdmin):
    list_display = ['title', 'product']

@admin.register(CharacteristicValue)
class CharacteristicValueAdmin(admin.ModelAdmin):
    list_display = ['title', 'characteristic']

class OrderItemInLine(admin.TabularInline):
    model = OrderItem
    extra = 0

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name', 'statuc', 'total_price', 'created_at']
    list_filter = ['statuc']
    inlines = [OrderItemInLine]

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'image']

