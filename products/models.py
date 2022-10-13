from django.db import models


class Category(models.Model):
    parent_category = models.ForeignKey(
        "Category",
        related_name="category_children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    name = models.CharField(max_length=254, unique=True)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    category = models.ForeignKey(
        "Category",
        related_name="category_product_categories",
        on_delete=models.SET_NULL,
        null=True,
    )
    product = models.ForeignKey(
        "Product",
        related_name="product_product_categories",
        on_delete=models.SET_NULL,
        null=True,
    )

    class Meta:
        unique_together = (("product", "category"),)


class Product(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    product_number = models.CharField(max_length=250, unique=True)
    categories = models.ManyToManyField("Category", through="ProductCategory")

    def __str__(self):
        return self.name
