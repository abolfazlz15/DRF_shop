from django.db import models
from apps.product.models import Product


class StockRecord(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='stockrecords')
    sku = models.CharField(max_length=65, blank=True, null=True, unique=True)
    buy_price = models.PositiveBigIntegerField(null=True, blank=True)
    sale_price = models.PositiveBigIntegerField()
    num_stock = models.PositiveIntegerField()
    threshold_low_stack = models.PositiveIntegerField(null=True, blank=True)

    class Meta:
        verbose_name = 'Stock Record'
        verbose_name_plural = 'Stock Records'
