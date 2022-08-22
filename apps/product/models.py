from django.db import models
from ckeditor.fields import RichTextField
from django.urls import reverse

from apps.account.models import Account
from config import settings


class Timestemp(models.Model):
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class TypeCategory(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    type_category = models.ForeignKey(TypeCategory, on_delete=models.SET_NULL, null=True, related_name='type_category')
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Category(models.Model):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.SET_NULL, null=True, related_name='sub_category')
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name


class Brand(Timestemp):
    name = models.CharField(max_length=30)
    image = models.ImageField(upload_to='product/brands/')

    def __str__(self):
        return self.name


class Category_status(Timestemp):
    name = models.CharField(max_length=100)

    @property
    def normalize_title(self):
        return self.name.replace(' ', '').lower()

    def __str__(self):
        return self.name


class Product(Timestemp):
    STATUS = (
        (0, 'NEW'),
        (1, 'SALE'),
        (2, 'POPULAR'),
        (3, 'PREMIUM'),
    )
    status = models.IntegerField(choices=STATUS, default=0)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, null=True, blank=True)
    # description = RichTextField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})


class NewValue(models.Model):
    new_price = models.CharField(max_length=20)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.product.name


class AttributeDetail(Timestemp):
    attribute = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='attribute_detail')
    key = models.IntegerField()
    value = models.CharField(max_length=221)
    new_price = models.ForeignKey(NewValue, on_delete=models.SET_NULL, null=True, blank=True)
    made_in = models.CharField(max_length=50)  # ishlab chiqarilgan joy
    release_form = models.CharField(max_length=30)  # chiqarish shakli
    consists = RichTextField()
    capacity = models.CharField(max_length=20)  # sig'imi
    guarantee = models.CharField(max_length=30)  # muddat

    def __str__(self):
        return self.attribute.name


class ProductImage(Timestemp):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_images')
    image = models.ImageField(upload_to='product/product_image/')

    def __str__(self):
        return f'image of {self.product}'
