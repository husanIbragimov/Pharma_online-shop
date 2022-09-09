# Generated by Django 3.2.15 on 2022-09-09 10:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0012_alter_product_value'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='cart',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='order',
            name='cart',
        ),
        migrations.RemoveField(
            model_name='order',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='created_at',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='cartitem',
            name='summa',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='order',
            name='cart_items',
            field=models.ManyToManyField(to='cart.CartItem'),
        ),
        migrations.AddField(
            model_name='order',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='order',
            name='summa',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='order',
            name='zipcode',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='address',
            field=models.CharField(max_length=221),
        ),
        migrations.AlterField(
            model_name='order',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='order',
            name='note',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.IntegerField(choices=[(0, 'NEW'), (1, 'PROCESS'), (2, 'CANCELED'), (3, 'FINISHED')], default=0),
        ),
    ]
