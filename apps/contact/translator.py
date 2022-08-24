from modeltranslation.translator import translator, TranslationOptions
from .models import *


class GetInTouchTranslationOptions(TranslationOptions):
    fields = ('full_name', 'message')


translator.register(GetInTouch, GetInTouchTranslationOptions)
