from django.contrib import admin
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'username', 'gender', 'is_active')
    prepopulated_fields = {"slug": ("username",)}


admin.site.register(Account, AccountAdmin)
