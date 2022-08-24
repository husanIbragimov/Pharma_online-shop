from modeltranslation.translator import translator, TranslationOptions
from .models import Article


class ArticleTranslationOptions(TranslationOptions):
    fields = ('title', 'slug', 'content')


translator.register(Article, ArticleTranslationOptions)
