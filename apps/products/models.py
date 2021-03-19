from django.db import models


class ProductsModel(models.Model):
    NEW = 'NEW'
    USED = 'USED'
    EXPIRED = 'EXPIRED'
    STATUS = (
        (NEW, 'NEW'),
        (USED, 'USED'),
        (EXPIRED, 'EXPIRED'),
    )
    name = models.CharField(max_length=100)
    sku = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=10, choices=STATUS, default=NEW)
    is_active = models.BooleanField(default=True)