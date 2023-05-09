from django.db import models
from apps.store.models import Product
class Order(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    address = models.CharField(max_length=128)
    zipcode = models.CharField(max_length=128)
    place = models.CharField(max_length=128)

    createAt = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paidAmount = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class OrederItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.DO_NOTHING)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.id}"

