from django.db import models


class Item(models.Model):
    """Товары на сайте"""
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField(max_length=512)
    price = models.IntegerField(blank=False)

    class Meta:
        db_table = 'item'
