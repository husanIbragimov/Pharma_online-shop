# Generated by Django 3.2.15 on 2022-09-06 07:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_auto_20220905_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]