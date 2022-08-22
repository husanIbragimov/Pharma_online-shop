from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from ..product.models import Timestemp


class Article(Timestemp):
    title = models.CharField(max_length=221)
    slug = models.SlugField(unique=True, null=True)
    image = models.ImageField(upload_to='articles/blog_image/')
    content = RichTextField()

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

