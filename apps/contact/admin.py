from django.contrib import admin
from .models import GetInTouch
from modeltranslation.admin import TranslationAdmin


class GetInTouchAdmin(TranslationAdmin):
    list_display = ('id', 'full_name', 'finished')


admin.site.register(GetInTouch, GetInTouchAdmin)
