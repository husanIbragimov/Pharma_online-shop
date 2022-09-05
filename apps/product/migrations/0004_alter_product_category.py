# Generated by Django 3.2.15 on 2022-09-05 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, limit_choices_to={'font_type__lt': 2}, to='product.Category'),
        ),
    ]
