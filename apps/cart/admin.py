from django.contrib import admin
from .models import *


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'quantity', 'phone', 'status',)
    readonly_fields = ('created_at',)


# admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(WishList)
admin.site.register(Order, OrderAdmin)

