from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

UNITS = (
    ('kg', 'kilogram'),
    ('g', 'gram'),
    ('mg', 'milligram'),
    ('lb', 'pound'),
    ('l', 'liter'),
    ('oz', 'ounce'),
    ('gr', 'grain'),
    ('bt', 'bottle'),
    ('bag', 'bag'),
    ('can', 'can'),
)

# Create your models here.


class PurchaseLocation(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.TextField(max_length=255, blank=True)


class Item(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    image = models.TextField(max_length=255, blank=True)
    purchase_locations = models.ManyToManyField(PurchaseLocation)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("ingredient-detail", kwargs={"pk": self.id})


class Pantry(models.Model):
    name = models.CharField(max_length=50)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def all_items(self):
        return self.items.select_related("item")


class PantryItem(models.Model):
    pantry = models.ForeignKey(
        Pantry,
        related_name='items',
        on_delete=models.CASCADE
    )
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    units = models.CharField(
        max_length=5,
        choices=UNITS,
        default=UNITS[0][0]
    )

    class Meta:
        unique_together = ("pantry", "item")

    def __str__(self):
        return f"{self.item.name}"
