# Generated by Django 3.2.15 on 2022-09-05 06:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_rename_in_active_category_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='font_type',
            field=models.IntegerField(choices=[(0, 'text'), (1, 'parent node')], default=1),
        ),
        migrations.AlterField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, limit_choices_to={'font_type': 1}, null=True, on_delete=django.db.models.deletion.SET_NULL, to='product.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(blank=True, limit_choices_to={'font_type__lt': 1}, to='product.Category'),
        ),
    ]