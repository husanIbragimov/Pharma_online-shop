# Generated by Django 3.2.15 on 2022-09-13 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0015_alter_product_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='consists',
            field=models.TextField(),
        ),
    ]
