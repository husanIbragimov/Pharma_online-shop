import uuid
from django.db import models

from apps.account.models import Account
from apps.product.models import Product


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    summa = models.FloatField(default=0.0)

    @property
    def get_total(self):
        if self.product.sale > 0:
            self.summa = self.quantity * self.product.sale
            self.save()
            return self.summa
        self.summa = self.quantity * self.product.value
        self.save()
        return self.summa

    # def __str__(self):
    #     return self.product



class Order(models.Model):
    STATUS = (
        (0, 'NEW'),
        (1, 'PROCESS'),
        (2, 'CANCELED'),
        (3, 'FINISHED'),
    )

    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    cart_items = models.ManyToManyField(CartItem)
    quantity = models.IntegerField(default=1)
    summa = models.FloatField(default=0.0)
    client = models.ForeignKey(Account, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=21)
    address = models.CharField(max_length=221)
    zipcode = models.IntegerField()
    note = models.CharField(max_length=250, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def get_quantity(self):
        self.quantity = sum([item.quantity for item in self.cart_items.all()])
        self.save()
        return self.quantity

    @property
    def get_summa(self):
        self.summa = sum([product.summa for product in self.cart_items.all()])
        self.save()
        return self.summa

    def __str__(self):
        return f'order of {self.client}'
