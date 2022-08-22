from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


class AttributeDetailInline(admin.StackedInline):
    model = AttributeDetail
    extra = 1


class AttributeAdmin(admin.ModelAdmin):
    inlines = [AttributeDetailInline]


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline, AttributeDetailInline]
    list_display = ['name', 'id', 'status', 'brand']
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name', 'description']


admin.site.register(Brand)
admin.site.register(NewValue)
admin.site.register(TypeCategory)
admin.site.register(SubCategory)
admin.site.register(AttributeDetail)
admin.site.register(Category_status)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
