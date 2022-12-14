# Generated by Django 4.1.2 on 2022-12-03 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GetInTouch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=55)),
                ('full_name_en', models.CharField(max_length=55, null=True)),
                ('full_name_ru', models.CharField(max_length=55, null=True)),
                ('full_name_uz', models.CharField(max_length=55, null=True)),
                ('phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('message_en', models.TextField(null=True)),
                ('message_ru', models.TextField(null=True)),
                ('message_uz', models.TextField(null=True)),
                ('user_data', models.BooleanField(default=False)),
                ('finished', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
    ]
