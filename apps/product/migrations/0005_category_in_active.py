# Generated by Django 3.2.15 on 2022-09-05 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='in_active',
            field=models.BooleanField(default=True),
        ),
    ]