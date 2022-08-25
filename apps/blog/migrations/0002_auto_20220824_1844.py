# Generated by Django 3.2.15 on 2022-08-24 13:44

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='content_en',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='content_ru',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='content_uz',
            field=ckeditor.fields.RichTextField(null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='slug_en',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='article',
            name='slug_ru',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='article',
            name='slug_uz',
            field=models.SlugField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_en',
            field=models.CharField(max_length=221, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_ru',
            field=models.CharField(max_length=221, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='title_uz',
            field=models.CharField(max_length=221, null=True),
        ),
    ]