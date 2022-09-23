from django.contrib import admin
from .models import CartItem, Order


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'quantity', 'phone', 'status',)
    readonly_fields = ('cart_items', 'created_at',)


class CartAdmin(admin.ModelAdmin):
    list_display = ('id', 'product')


admin.site.register(CartItem, CartAdmin)
admin.site.register(Order, OrderAdmin)