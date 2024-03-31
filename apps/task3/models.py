from django.db import models

from apps.shared.models import AbstractModel


class Product(AbstractModel):
    price = models.DecimalField(max_digits=12, decimal_places=2)
    marja = models.DecimalField(max_digits=12, decimal_places=2)
    package_code = models.CharField(max_length=50)
    name = models.CharField(max_length=128, default="")
    description = models.TextField(default="")

    def __str__(self):
        return self.package_code
