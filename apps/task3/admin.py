from django.contrib import admin

from apps.task3.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "price")

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"
