from django.db import models


# CATEGORY CHOICES
CATEGORY_CHOICES = [
    ('pizza', 'Pizza'),
    ('burger', 'Burger'),
    ('fries', 'Fries'),
    ('sandwich', 'Sandwich'),
    ('shawarma', 'Shawarma'),
]


# SIZE CHOICES
SIZE_CHOICES = [
    ('small', 'Small'),
    ('medium', 'Medium'),
    ('large', 'Large'),
    ('regular', 'Regular'),
]


# ORDER OPTIONS
ORDER_TYPE_CHOICES = [
    ('takeaway', 'Take Away'),
    ('delivery', 'Delivery'),
    ('dining', 'Dining'),
]


class Product(models.Model):
    name = models.CharField(max_length=100)

    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES
    )

    size = models.CharField(
        max_length=10,
        choices=SIZE_CHOICES,
        default='regular'
    )

    price = models.DecimalField(max_digits=8, decimal_places=2)


    is_popular = models.BooleanField(default=False)

    order_type = models.CharField(
        max_length=20,
        choices=ORDER_TYPE_CHOICES,
        default='takeaway'
    )

    image = models.ImageField(upload_to='products/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.size})"