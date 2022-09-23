# Generated by Django 3.2.15 on 2022-09-12 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20220824_1844'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.CharField(db_index=True, default=1, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]