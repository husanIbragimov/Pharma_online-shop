from django.contrib import admin
from .models import GetInTouch


class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'finished')


admin.site.register(GetInTouch, GetInTouchAdmin)
