from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'parent_category', 'font_type', 'is_active')


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


# class AttributeDetailInline(admin.StackedInline):
#     model = AttributeDetail
#     extra = 1
#
#
# class AttributeAdmin(TranslationAdmin):
#     inlines = [AttributeDetailInline]


class ProductAdmin(TranslationAdmin):
    inlines = [ProductImageInline]
    list_display = ['name', 'id', 'status', 'brand', 'key']
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ['name', 'description']
    filter_horizontal = ('category',)


admin.site.register(Brand)
admin.site.register(NewValue)
admin.site.register(Banner)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
