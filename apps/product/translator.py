from modeltranslation.translator import translator, TranslationOptions
from .models import *


class TypeCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class SubCategoryTranslationOptions(TranslationOptions):
    fields = ('name',)


class CategoryTranslationOptions(TranslationOptions):
    pass


class ProductTranslationOptions(TranslationOptions):
    fields = ('name', 'slug',)


# class AttributeDetailTranslationOptions(TranslationOptions):
#     fields = ('made_in', 'release_form', 'consists', 'capacity', 'guarantee')


# translator.register(AttributeDetail, AttributeDetailTranslationOptions)
# translator.register(TypeCategory, TypeCategoryTranslationOptions)
# translator.register(SubCategory, SubCategoryTranslationOptions)
# translator.register(Category, CategoryTranslationOptions)
translator.register(Product, ProductTranslationOptions)
