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


class Category(Timestemp):
    FONT_TYPE = (
        (0, 'text'),
        (1, 'parent node'),

    )
    name = models.CharField(max_length=100)
    parent_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True,
                                        limit_choices_to={'font_type': 1})
    font_type = models.IntegerField(choices=FONT_TYPE, default=1)
    is_active = models.BooleanField(default=True)

    @property
    def normalize_title(self):
        return self.name.replace(' ', '').lower()

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


class NewValue(models.Model):
    new_price = models.CharField(max_length=20)

    def __str__(self):
        return self.new_price


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
    category = models.ManyToManyField(Category, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True, blank=True)
    key = models.CharField(max_length=30, null=True)
    value = models.IntegerField()
    new_price = models.ForeignKey(NewValue, on_delete=models.SET_NULL, null=True, blank=True)
    made_in = models.CharField(max_length=50)  # ishlab chiqarilgan joy
    release_form = models.CharField(max_length=30)  # chiqarish shakli
    consists = RichTextField()
    capacity = models.CharField(max_length=20)  # sig'imi
    guarantee = models.CharField(max_length=30)  # muddat
    is_active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return f'{self.name} | {self.id}'


class ProductImage(Timestemp):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, related_name='product_images')
    image = models.ImageField(upload_to='product/product_image/')
    is_active = models.BooleanField(default=True)

    @property
    def get_image_url(self):
        if settings.DEBUG:
            return f"{settings.LOCAL_BASE_URL}{self.image.url}"
        else:
            return f"{settings.PROD_BASE_URL}{self.image.url}"

    def __str__(self):
        return f'image of {self.product.id}'
