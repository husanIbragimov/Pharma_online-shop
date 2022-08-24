import uuid

from django.conf import settings
from django.db import models
from ..product.models import Timestemp, Product, AttributeDetail
from ..account.models import Account


class WishList(Timestemp):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f'wishlist of {self.user.email} (id: {self.id})'


class Cart(Timestemp):
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    is_ordered = models.BooleanField(default=False)

    @property
    def get_cart_items(self):
        cart_items = self.cart_items.all()
        total = sum([item.quantity for item in cart_items])
        return total

    @property
    def get_cart_total(self):
        cart_items = self.cart_items.all()
        total = sum([item.get_total for item in cart_items])
        return total

    def __str__(self):
        return f'{self.client} (id:{self.id})'


class CartItem(Timestemp):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='cart_items')
    product_detail = models.ForeignKey(AttributeDetail, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, null=True)

    @property
    def get_total(self):
        return self.quantity * self.product_detail.value


class Order(Timestemp):
    STATUS = (
        (0, 'NEW'),
        (1, 'PROCESS'),
        (2, 'FINISHED'),
        (3, 'CANCELED'),
    )
    transaction_id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=21)
    address = models.CharField(max_length=100)
    note = models.CharField(max_length=200, null=True, blank=True)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self):
        return f'order of {self.client} | {self.transaction_id}'
